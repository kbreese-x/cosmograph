---
tags: [gradio-custom-component, ]
title: gradio_cosmograph
short_description: cosmosgraph viewer component
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# `gradio_cosmograph`
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  

cosmosgraph viewer component

## Installation

```bash
pip install gradio_cosmograph
```

## Usage

```python
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

```

## `NetworkGraph`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
dict[str, typing.Any] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">A dictionary containing the graph data with 'nodes' and 'links' lists. Each node should have an 'id' property</td>
</tr>

<tr>
<td align="left"><code>background_color</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">The color of the graph background. Accepts any valid CSS color string.</td>
</tr>

<tr>
<td align="left"><code>node_size_scale</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>1.0</code></td>
<td align="left">Scale factor for all node sizes. Default is 1.0.</td>
</tr>

<tr>
<td align="left"><code>link_width_scale</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>1.0</code></td>
<td align="left">Scale factor for all link widths. Default is 1.0.</td>
</tr>

<tr>
<td align="left"><code>scale_nodes_on_zoom</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">Whether nodes should scale when zooming. Default is True.</td>
</tr>

<tr>
<td align="left"><code>pixel_ratio</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>2.0</code></td>
<td align="left">Canvas pixel ratio for rendering quality. Default is 2.0.</td>
</tr>

<tr>
<td align="left"><code>node_greyout_opacity</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>0.1</code></td>
<td align="left">Opacity of unselected nodes when selection is active (0-1). Default is 0.1.</td>
</tr>

<tr>
<td align="left"><code>focused_node_ring_color</code></td>
<td align="left" style="width: 25%;">

```python
str
```

</td>
<td align="left"><code>"white"</code></td>
<td align="left">Color of the ring around focused nodes. Default is "white".</td>
</tr>

<tr>
<td align="left"><code>render_hovered_node_ring</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">Whether to show a ring around hovered nodes. Default is True.</td>
</tr>

<tr>
<td align="left"><code>hovered_node_ring_color</code></td>
<td align="left" style="width: 25%;">

```python
str
```

</td>
<td align="left"><code>"white"</code></td>
<td align="left">Color of the ring around hovered nodes. Default is "white".</td>
</tr>

<tr>
<td align="left"><code>render_links</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">Whether to render links between nodes. Default is True.</td>
</tr>

<tr>
<td align="left"><code>link_arrows</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">Whether to show arrows on links. Default is True.</td>
</tr>

<tr>
<td align="left"><code>link_arrows_size_scale</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>1.0</code></td>
<td align="left">Scale factor for link arrow size. Default is 1.0.</td>
</tr>

<tr>
<td align="left"><code>link_greyout_opacity</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>0.1</code></td>
<td align="left">Opacity of unselected links when selection is active (0-1). Default is 0.1.</td>
</tr>

<tr>
<td align="left"><code>curved_links</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">Whether to render curved links. Default is False.</td>
</tr>

<tr>
<td align="left"><code>curved_link_segments</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>19</code></td>
<td align="left">Number of segments in curved links. Default is 19.</td>
</tr>

<tr>
<td align="left"><code>curved_link_weight</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>0.8</code></td>
<td align="left">Weight factor for curve shape (0-1). Default is 0.8.</td>
</tr>

<tr>
<td align="left"><code>curved_link_control_point_distance</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>0.5</code></td>
<td align="left">Distance of curve control point. Default is 0.5.</td>
</tr>

<tr>
<td align="left"><code>link_visibility_min_transparency</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>0.25</code></td>
<td align="left">Minimum transparency for long links. Default is 0.25.</td>
</tr>

<tr>
<td align="left"><code>link_visibility_distance_range</code></td>
<td align="left" style="width: 25%;">

```python
tuple[float, float]
```

</td>
<td align="left"><code>50, 150</code></td>
<td align="left">Range for link length-based transparency (min, max). Default is (50, 150).</td>
</tr>

<tr>
<td align="left"><code>node_label_key</code></td>
<td align="left" style="width: 25%;">

```python
str
```

</td>
<td align="left"><code>"id"</code></td>
<td align="left">Key from node data to use as label text. Default is "id".</td>
</tr>

<tr>
<td align="left"><code>show_dynamic_labels</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">Whether to show labels while zooming. Default is True.</td>
</tr>

<tr>
<td align="left"><code>show_top_labels</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">Whether to show labels for top nodes. Default is False.</td>
</tr>

<tr>
<td align="left"><code>show_top_labels_limit</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>100</code></td>
<td align="left">Maximum number of top labels to show. Default is 100.</td>
</tr>

<tr>
<td align="left"><code>show_hovered_node_label</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">Whether to show label for hovered node. Default is True.</td>
</tr>

<tr>
<td align="left"><code>disable_zoom</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True, prevents zooming and panning. Default is False.</td>
</tr>

<tr>
<td align="left"><code>initial_zoom_level</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>1.0</code></td>
<td align="left">Starting zoom level. Default is 1.0.</td>
</tr>

<tr>
<td align="left"><code>fit_view_on_init</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">Whether to fit view to all nodes on init. Default is True.</td>
</tr>

<tr>
<td align="left"><code>fit_view_delay</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>250</code></td>
<td align="left">Delay before fitting view on init (ms). Default is 250.</td>
</tr>

<tr>
<td align="left"><code>disable_simulation</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True, nodes won't move after placement. Default is False.</td>
</tr>

<tr>
<td align="left"><code>space_size</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>4096</code></td>
<td align="left">Size of simulation space (max 8192). Default is 4096.</td>
</tr>

<tr>
<td align="left"><code>simulation_decay</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>1000</code></td>
<td align="left">Force simulation decay coefficient. Default is 1000.</td>
</tr>

<tr>
<td align="left"><code>simulation_friction</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>0.85</code></td>
<td align="left">Friction coefficient (0.8-1.0). Default is 0.85.</td>
</tr>

<tr>
<td align="left"><code>simulation_repulsion</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>0.1</code></td>
<td align="left">Node repulsion force (0.0-2.0). Default is 0.1.</td>
</tr>

<tr>
<td align="left"><code>simulation_repulsion_theta</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>1.7</code></td>
<td align="left">Barnes-Hut approximation criterion (0.3-2.0). Default is 1.7.</td>
</tr>

<tr>
<td align="left"><code>simulation_link_spring</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>1.0</code></td>
<td align="left">Link spring force (0.0-2.0). Default is 1.0.</td>
</tr>

<tr>
<td align="left"><code>simulation_link_distance</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>2.0</code></td>
<td align="left">Minimum distance between linked nodes. Default is 2.0.</td>
</tr>

<tr>
<td align="left"><code>simulation_gravity</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>0.0</code></td>
<td align="left">Gravity force toward center (0.0-1.0). Default is 0.0.</td>
</tr>

<tr>
<td align="left"><code>simulation_center</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>0.0</code></td>
<td align="left">Centering force (0.0-1.0). Default is 0.0.</td>
</tr>

<tr>
<td align="left"><code>simulation_repulsion_from_mouse</code></td>
<td align="left" style="width: 25%;">

```python
float
```

</td>
<td align="left"><code>2.0</code></td>
<td align="left">Mouse repulsion force (0.0-5.0). Default is 2.0.</td>
</tr>

<tr>
<td align="left"><code>use_quadtree</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">Whether to use quadtree algorithm. Default is False.</td>
</tr>

<tr>
<td align="left"><code>repulsion_quadtree_levels</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>12</code></td>
<td align="left">Depth of quadtree approximation. Default is 12.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | gradio.i18n.I18nData | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Component label shown in UI.</td>
</tr>

<tr>
<td align="left"><code>info</code></td>
<td align="left" style="width: 25%;">

```python
str | gradio.i18n.I18nData | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Tooltip information text.</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Number of seconds between value updates.</td>
</tr>

<tr>
<td align="left"><code>inputs</code></td>
<td align="left" style="width: 25%;">

```python
gradio.components.base.Component
    | Sequence[gradio.components.base.Component]
    | set[gradio.components.base.Component]
    | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Components that trigger value updates.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">Whether to show the component label.</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">Whether to use container styling.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Relative width compared to other components.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">Minimum pixel width.</td>
</tr>

<tr>
<td align="left"><code>min_height</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">Whether component is visible.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">HTML element ID.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">HTML element classes.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">Whether to render in Blocks context.</td>
</tr>

<tr>
<td align="left"><code>key</code></td>
<td align="left" style="width: 25%;">

```python
int | str | tuple[int | str, Ellipsis] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">Unique key for component identity across renders.</td>
</tr>

<tr>
<td align="left"><code>preserved_by_key</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>"value"</code></td>
<td align="left">Parameters to preserve across re-renders.</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the NetworkGraph changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |



