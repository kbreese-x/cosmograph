import colorsys
import hashlib
import os
from typing import Any, Dict, List
import pandas as pd

from dotenv import load_dotenv
from neo4j import GraphDatabase, Transaction
from neo4j.graph import Graph, Node

load_dotenv()

NEO4J_BOLT_EXTERNAL_PORT = os.getenv("NEO4J_BOLT_EXTERNAL_PORT", "7687")
NEO4J_URI = f"bolt://localhost:{NEO4J_BOLT_EXTERNAL_PORT}"
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")

NEO4J_DRIVER = GraphDatabase.driver(
    NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD), database=NEO4J_DATABASE
)


def _read_graph(tx: Transaction, query: str, params: dict[str, Any]) -> Graph:
    """Execute a read query and return the results as a JSON string"""
    raw_results = tx.run(query, params if params else {})
    graph_results = raw_results.graph()
    return graph_results


def _read_data(
    tx: Transaction, query: str, params: dict[str, Any]
) -> List[Dict[str, Any]]:
    """Execute a read query and return the results as a list of dictionaries"""
    raw_results = tx.run(query, params if params else {})
    return raw_results.data()


def _read_dataframe(
    tx: Transaction, query: str, params: dict[str, Any]
) -> pd.DataFrame:
    """Execute a read query and return the results as a JSON string"""
    raw_results = tx.run(query, params if params else {})
    df = raw_results.to_df()
    return df


def run_query(query: str, parameters: Dict[str, Any] = {}) -> Dict[str, Any]:
    with NEO4J_DRIVER.session() as session:
        graph = session.execute_read(_read_graph, query, parameters)
        if len(graph.nodes) == 0 or len(graph.relationships) == 0:
            graph = None

        data = session.execute_read(_read_dataframe, query, parameters)

        return {
            "data": data,
            "graph": graph,
        }


def get_node_label_color(label: str) -> str:
    """Generate a consistent color for a given node label."""
    # Use hash of label to generate a consistent hue
    label_hash = int(hashlib.md5(label.encode()).hexdigest(), 16)
    hue = (label_hash % 1000) / 1000.0  # Convert hash to value between 0 and 1
    # Create a pastel color with high saturation but moderate brightness
    rgb = colorsys.hsv_to_rgb(hue, 0.7, 0.9)
    # Convert to hex color
    return f"#{int(rgb[0] * 255):02x}{int(rgb[1] * 255):02x}{int(rgb[2] * 255):02x}"


def get_node_display_name(node: Node) -> str:
    """
    Extract a display name from node properties, prioritizing properties containing 'name',
    then falling back to node labels.

    Args:
        node: Neo4j Node object

    Returns:
        str: Display name for the node
    """
    # First check for properties containing 'name' (case insensitive)
    name_props = [key for key in node.keys() if "name" in key.lower()]
    if name_props:
        # If multiple matches, prefer exact 'name' match, otherwise take first
        if "name" in name_props:
            return str(node["name"])
        return str(node[name_props[0]])

    # If no name property found, try using the node label
    if node.labels:
        return str(next(iter(node.labels)))

    # Fallback to element ID if no properties or labels
    return f"Node-{node.element_id}"


def neo4j_graph_to_cosmograph(graph: Graph) -> dict:
    """
    Convert a Neo4j Graph object to Cosmograph-compatible format.

    Args:
        graph: Neo4j Graph object containing nodes and relationships

    Returns:
        dict: Dictionary containing 'nodes' and 'links' lists compatible with Cosmograph
    """
    nodes = []
    node_id_map = {}  # Map Neo4j element_ids to array indices

    # Process nodes
    for i, node in enumerate(graph.nodes):
        # Store the mapping of Neo4j element_id to array index
        node_id_map[node.element_id] = i

        # Get the first label (if any) for color assignment
        label = next(iter(node.labels)) if node.labels else "Unknown"

        # Create node object
        node_obj = {
            "id": str(i),  # Cosmograph needs string IDs
            "label": label,
            "displayName": get_node_display_name(node),
            "color": get_node_label_color(label),
            # "size": 5,  # Default size, could be made dynamic based on node properties
            "properties": dict(node.items()),  # Store all original properties
        }
        nodes.append(node_obj)

    # Process relationships
    links = []
    for rel in graph.relationships:
        start_node, end_node = rel.nodes

        # Only create link if both nodes exist
        if (
            start_node
            and end_node
            and start_node.element_id in node_id_map
            and end_node.element_id in node_id_map
        ):
            link_obj = {
                "source": str(node_id_map[start_node.element_id]),
                "target": str(node_id_map[end_node.element_id]),
                "type": rel.type,
                "properties": dict(rel.items()),
                # "color": "#000000",  # Default link color
                # "width": 5,  # Default link width
            }
            links.append(link_obj)

    return {"nodes": nodes, "links": links}
