from pathlib import Path

import gradio as gr
import gradio.themes as themes
from gradio_cosmograph import NetworkGraph

from components import *
from utils import *

sample_data = {
    "nodes": [
        {"id": "Kai", "label": "Kai (You)", "color": "#f97316", "size": 5},
        {"id": "ChatGPT", "label": "LLM Assistant", "color": "#3b82f6", "size": 5},
        {"id": "Project", "label": "Codebot Project", "color": "#22c55e", "size": 5},
        {"id": "AWS", "label": "AWS Cloud", "color": "#facc15", "size": 5},
        {"id": "Gradio", "label": "Gradio UI", "color": "#a855f7", "size": 5},
        {"id": "Cosmograph", "label": "GPU Graph Lib", "color": "#ec4899", "size": 5},
        {"id": "LangChain", "label": "LangChain", "color": "#0ea5e9", "size": 5},
        {"id": "S3", "label": "S3 Bucket", "color": "#ef4444", "size": 5},
        {"id": "Lambda", "label": "AWS Lambda", "color": "#14b8a6", "size": 5},
        {"id": "SageMaker", "label": "SageMaker Endpt.", "color": "#64748b", "size": 5},
        {"id": "Alice", "label": "Random User A", "color": "#fb923c", "size": 5},
        {"id": "Bob", "label": "Random User B", "color": "#60a5fa", "size": 5},
    ],
    "links": [
        {"source": "Kai", "target": "Project", "weight": 2, "label": "leads"},
        {"source": "Project", "target": "Gradio", "weight": 1},
        {"source": "Project", "target": "Cosmograph", "weight": 1},
        {"source": "Project", "target": "LangChain", "weight": 1},
        {"source": "Project", "target": "AWS", "weight": 1},
        {"source": "AWS", "target": "S3", "weight": 1},
        {"source": "AWS", "target": "Lambda", "weight": 1},
        {"source": "AWS", "target": "SageMaker", "weight": 1},
        {"source": "ChatGPT", "target": "Kai", "weight": 3, "label": "assists"},
        {"source": "LangChain", "target": "SageMaker", "weight": 1},
        {"source": "Lambda", "target": "SageMaker", "weight": 1},
        {"source": "Alice", "target": "Bob", "weight": 1},
    ],
}

# Constants
NA = "N/A"

GET_SCHEMA_CYPHER = """
CALL apoc.meta.data() YIELD label, property, type, other, unique, index, elementType
WHERE elementType = 'node' AND NOT label STARTS WITH '_'
WITH label, 
COLLECT(CASE WHEN type <> 'RELATIONSHIP' THEN [property, type + CASE WHEN unique THEN " unique" ELSE "" END + CASE WHEN index THEN " indexed" ELSE "" END] END) AS attributes,
COLLECT(CASE WHEN type = 'RELATIONSHIP' THEN [property, head(other)] END) AS relationships
RETURN label, apoc.map.fromPairs(attributes) AS attributes, apoc.map.fromPairs(relationships) AS relationships
"""

GET_SCHEMA_GRAPH_CYPHER = "CALL db.schema.visualization()"

LIST_PAYORS_CYPHER = "MATCH (p:Payor) RETURN p;"

LIST_PAYOR_DOCUMENTS_CYPHER = """
MATCH (p1:Payor) WHERE p1.name = 'uhc' 
MATCH (p1)-[:OFFERS]->(p2:Plan) 
MATCH (p2)-[:PUBLISHES]->(d:Document) 
RETURN p2.name, d.fileName
"""

LIST_PAYOR_DOCUMENTS_GRAPH_CYPHER = """
MATCH (p1:Payor) WHERE p1.name = 'uhc' 
MATCH (p1)-[o:OFFERS]->(p2:Plan)-[pub:PUBLISHES]->(d:Document)-[h]->(x)
RETURN *
"""


with gr.Blocks(
    theme=themes.Glass(
        # primary_hue=themes.colors.blue, secondary_hue=themes.colors.sky
    ),
    fill_height=True,
    title="Prior Authorization Demo",
) as demo:
    with gr.Row():
        gr.Image(
            str(Path(__file__).parent / "assets" / "logo.png"),
            show_label=False,
            container=False,
            show_download_button=False,
            show_share_button=False,
            show_fullscreen_button=False,
            # width=200,
            min_width=300,
            scale=0,
            elem_id="logo",
        )
        title = create_title("Prior Authorization Demo")

    with gr.Row(
        equal_height=True,
        scale=0,
        height="75vh",
    ):
        with gr.Column(scale=2, variant="panel") as input_column:
            with gr.Row(variant="compact"):
                payor_dropdown = gr.Dropdown(
                    label="Payor",
                    choices=["UHC"],
                    interactive=True,
                )
                plan_dropdown = gr.Dropdown(
                    label="Plan Name",
                    choices=["UHC"],
                    interactive=True,
                )
            with gr.Row(variant="compact"):
                cpt_dropdown = gr.Dropdown(
                    label="CPT Code",
                    allow_custom_value=True,
                    interactive=True,
                )
                icd_dropdown = gr.Dropdown(
                    label="ICD Code",
                    allow_custom_value=True,
                    interactive=True,
                )
            with gr.Row(variant="compact"):
                state_dropdown = gr.Dropdown(
                    label="State",
                    choices=LIST_OF_STATES,
                    value="CA",
                    interactive=True,
                )
                age_dropdown = gr.Dropdown(
                    label="Patient Age",
                    choices=[i for i in range(1, 100)],
                    value=None,
                    interactive=True,
                )
                gender_dropdown = gr.Dropdown(
                    label="Gender",
                    choices=["M", "F", "Other"],
                    interactive=True,
                )
            with gr.Row(variant="compact"):
                svc_code_dropdown = gr.Dropdown(
                    label="SVC Code",
                    value=NA,
                    allow_custom_value=True,
                    interactive=True,
                )
                physician_dropdown = gr.Dropdown(
                    label="Ordering Physician",
                    value=NA,
                    allow_custom_value=True,
                    interactive=True,
                )
            with gr.Row():
                upload_btn = gr.UploadButton("Upload File")
                submit_btn = gr.Button("Check for PA", variant="primary")

        with gr.Column(scale=3, variant="panel") as output_column:
            with gr.Tab("View Graph"):
                with gr.Row(variant="panel"):
                    cypher_component = gr.Code(
                        label="Cypher Query",
                        value=LIST_PAYOR_DOCUMENTS_GRAPH_CYPHER,
                        # placeholder="Enter Cypher query here...",
                        interactive=True,
                        lines=5,
                        show_line_numbers=False,
                        language="sql",
                        container=False,
                    )
                    run_query_btn = gr.Button("Run Query", variant="primary", scale=0)

                graph_component = NetworkGraph(
                    value=sample_data,
                    # show_top_labels_limit=3,
                    show_dynamic_labels=False,
                    show_top_labels=False,
                    node_label_key="displayName",
                    # simulation_repulsion=0.4,
                    background_color="#d3d3d3",
                    # simulation_friction=0.8,
                    simulation_link_distance=10,
                    # simulation_link_spring=1.5,
                    min_height=500,
                )
                dataframe = gr.Dataframe(visible=False)

                @run_query_btn.click(
                    inputs=cypher_component,
                    outputs=[graph_component, dataframe],
                )
                def run_cypher_query(cypher_query):
                    result = run_query(
                        query=cypher_query,
                        parameters={},
                    )
                    if result["graph"]:
                        graph_data = neo4j_graph_to_cosmograph(result["graph"])
                        # print(graph_data)
                        return gr.update(value=graph_data, visible=True), gr.DataFrame(
                            visible=False
                        )
                    else:
                        return gr.update(visible=False), gr.Dataframe(
                            result["data"], visible=True
                        )

            with gr.Tab("Model Interpretation"):
                messages_component = gr.Chatbot(type="messages")
                bedrock_messages = gr.State([])  # State to hold chat messages

            with gr.Row():
                view_requirements_btn = gr.Button(
                    "View PA Requirement Doc",
                    variant="primary",
                )
                view_coverage_rationale_btn = gr.Button(
                    "View Coverage Rationale Doc",
                    variant="primary",
                )
                view_medical_records_btn = gr.Button(
                    "View Medical Records Doc",
                    variant="primary",
                )


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")
