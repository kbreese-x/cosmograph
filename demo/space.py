
import gradio as gr
from app import demo as app
import os

_docs = {'NetworkGraph': {'description': 'Creates a network graph visualization component using Cosmograph. Can be used to display node-link diagrams\nwith customizable styling and interaction options.', 'members': {'__init__': {'value': {'type': 'dict[str, typing.Any] | None', 'default': 'None', 'description': "A dictionary containing the graph data with 'nodes' and 'links' lists. Each node should have an 'id' property"}, 'background_color': {'type': 'str | None', 'default': 'None', 'description': 'The color of the graph background. Accepts any valid CSS color string.'}, 'node_size_scale': {'type': 'float', 'default': '1.0', 'description': 'Scale factor for all node sizes. Default is 1.0.'}, 'link_width_scale': {'type': 'float', 'default': '1.0', 'description': 'Scale factor for all link widths. Default is 1.0.'}, 'scale_nodes_on_zoom': {'type': 'bool', 'default': 'True', 'description': 'Whether nodes should scale when zooming. Default is True.'}, 'pixel_ratio': {'type': 'float', 'default': '2.0', 'description': 'Canvas pixel ratio for rendering quality. Default is 2.0.'}, 'node_greyout_opacity': {'type': 'float', 'default': '0.1', 'description': 'Opacity of unselected nodes when selection is active (0-1). Default is 0.1.'}, 'focused_node_ring_color': {'type': 'str', 'default': '"white"', 'description': 'Color of the ring around focused nodes. Default is "white".'}, 'render_hovered_node_ring': {'type': 'bool', 'default': 'True', 'description': 'Whether to show a ring around hovered nodes. Default is True.'}, 'hovered_node_ring_color': {'type': 'str', 'default': '"white"', 'description': 'Color of the ring around hovered nodes. Default is "white".'}, 'render_links': {'type': 'bool', 'default': 'True', 'description': 'Whether to render links between nodes. Default is True.'}, 'link_arrows': {'type': 'bool', 'default': 'True', 'description': 'Whether to show arrows on links. Default is True.'}, 'link_arrows_size_scale': {'type': 'float', 'default': '1.0', 'description': 'Scale factor for link arrow size. Default is 1.0.'}, 'link_greyout_opacity': {'type': 'float', 'default': '0.1', 'description': 'Opacity of unselected links when selection is active (0-1). Default is 0.1.'}, 'curved_links': {'type': 'bool', 'default': 'False', 'description': 'Whether to render curved links. Default is False.'}, 'curved_link_segments': {'type': 'int', 'default': '19', 'description': 'Number of segments in curved links. Default is 19.'}, 'curved_link_weight': {'type': 'float', 'default': '0.8', 'description': 'Weight factor for curve shape (0-1). Default is 0.8.'}, 'curved_link_control_point_distance': {'type': 'float', 'default': '0.5', 'description': 'Distance of curve control point. Default is 0.5.'}, 'link_visibility_min_transparency': {'type': 'float', 'default': '0.25', 'description': 'Minimum transparency for long links. Default is 0.25.'}, 'link_visibility_distance_range': {'type': 'tuple[float, float]', 'default': '50, 150', 'description': 'Range for link length-based transparency (min, max). Default is (50, 150).'}, 'node_label_key': {'type': 'str', 'default': '"id"', 'description': 'Key from node data to use as label text. Default is "id".'}, 'show_dynamic_labels': {'type': 'bool', 'default': 'True', 'description': 'Whether to show labels while zooming. Default is True.'}, 'show_top_labels': {'type': 'bool', 'default': 'True', 'description': 'Whether to show labels for top nodes. Default is False.'}, 'show_top_labels_limit': {'type': 'int', 'default': '100', 'description': 'Maximum number of top labels to show. Default is 100.'}, 'show_hovered_node_label': {'type': 'bool', 'default': 'True', 'description': 'Whether to show label for hovered node. Default is True.'}, 'disable_zoom': {'type': 'bool', 'default': 'False', 'description': 'If True, prevents zooming and panning. Default is False.'}, 'initial_zoom_level': {'type': 'float', 'default': '1.0', 'description': 'Starting zoom level. Default is 1.0.'}, 'fit_view_on_init': {'type': 'bool', 'default': 'True', 'description': 'Whether to fit view to all nodes on init. Default is True.'}, 'fit_view_delay': {'type': 'int', 'default': '250', 'description': 'Delay before fitting view on init (ms). Default is 250.'}, 'disable_simulation': {'type': 'bool', 'default': 'False', 'description': "If True, nodes won't move after placement. Default is False."}, 'space_size': {'type': 'int', 'default': '4096', 'description': 'Size of simulation space (max 8192). Default is 4096.'}, 'simulation_decay': {'type': 'int', 'default': '1000', 'description': 'Force simulation decay coefficient. Default is 1000.'}, 'simulation_friction': {'type': 'float', 'default': '0.85', 'description': 'Friction coefficient (0.8-1.0). Default is 0.85.'}, 'simulation_repulsion': {'type': 'float', 'default': '0.1', 'description': 'Node repulsion force (0.0-2.0). Default is 0.1.'}, 'simulation_repulsion_theta': {'type': 'float', 'default': '1.7', 'description': 'Barnes-Hut approximation criterion (0.3-2.0). Default is 1.7.'}, 'simulation_link_spring': {'type': 'float', 'default': '1.0', 'description': 'Link spring force (0.0-2.0). Default is 1.0.'}, 'simulation_link_distance': {'type': 'float', 'default': '2.0', 'description': 'Minimum distance between linked nodes. Default is 2.0.'}, 'simulation_gravity': {'type': 'float', 'default': '0.0', 'description': 'Gravity force toward center (0.0-1.0). Default is 0.0.'}, 'simulation_center': {'type': 'float', 'default': '0.0', 'description': 'Centering force (0.0-1.0). Default is 0.0.'}, 'simulation_repulsion_from_mouse': {'type': 'float', 'default': '2.0', 'description': 'Mouse repulsion force (0.0-5.0). Default is 2.0.'}, 'use_quadtree': {'type': 'bool', 'default': 'False', 'description': 'Whether to use quadtree algorithm. Default is False.'}, 'repulsion_quadtree_levels': {'type': 'int', 'default': '12', 'description': 'Depth of quadtree approximation. Default is 12.'}, 'label': {'type': 'str | gradio.i18n.I18nData | None', 'default': 'None', 'description': 'Component label shown in UI.'}, 'info': {'type': 'str | gradio.i18n.I18nData | None', 'default': 'None', 'description': 'Tooltip information text.'}, 'every': {'type': 'float | None', 'default': 'None', 'description': 'Number of seconds between value updates.'}, 'inputs': {'type': 'gradio.components.base.Component\n    | Sequence[gradio.components.base.Component]\n    | set[gradio.components.base.Component]\n    | None', 'default': 'None', 'description': 'Components that trigger value updates.'}, 'show_label': {'type': 'bool', 'default': 'True', 'description': 'Whether to show the component label.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'Whether to use container styling.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'Relative width compared to other components.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'Minimum pixel width.'}, 'min_height': {'type': 'int', 'default': '160', 'description': None}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'Whether component is visible.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'HTML element ID.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'HTML element classes.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'Whether to render in Blocks context.'}, 'key': {'type': 'int | str | tuple[int | str, Ellipsis] | None', 'default': 'None', 'description': 'Unique key for component identity across renders.'}, 'preserved_by_key': {'type': 'list[str] | str | None', 'default': '"value"', 'description': 'Parameters to preserve across re-renders.'}}, 'postprocess': {}, 'preprocess': {}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the NetworkGraph changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}}}, '__meta__': {'additional_interfaces': {}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_cosmograph`

<div style="display: flex; gap: 7px;">
<img alt="Static Badge" src="https://img.shields.io/badge/version%20-%200.0.1%20-%20orange">  
</div>

cosmosgraph viewer component
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
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

GET_SCHEMA_CYPHER = \"\"\"
CALL apoc.meta.data() YIELD label, property, type, other, unique, index, elementType
WHERE elementType = 'node' AND NOT label STARTS WITH '_'
WITH label, 
COLLECT(CASE WHEN type <> 'RELATIONSHIP' THEN [property, type + CASE WHEN unique THEN " unique" ELSE "" END + CASE WHEN index THEN " indexed" ELSE "" END] END) AS attributes,
COLLECT(CASE WHEN type = 'RELATIONSHIP' THEN [property, head(other)] END) AS relationships
RETURN label, apoc.map.fromPairs(attributes) AS attributes, apoc.map.fromPairs(relationships) AS relationships
\"\"\"

GET_SCHEMA_GRAPH_CYPHER = "CALL db.schema.visualization()"

LIST_PAYORS_CYPHER = "MATCH (p:Payor) RETURN p;"

LIST_PAYOR_DOCUMENTS_CYPHER = \"\"\"
MATCH (p1:Payor) WHERE p1.name = 'uhc' 
MATCH (p1)-[:OFFERS]->(p2:Plan) 
MATCH (p2)-[:PUBLISHES]->(d:Document) 
RETURN p2.name, d.fileName
\"\"\"

LIST_PAYOR_DOCUMENTS_GRAPH_CYPHER = \"\"\"
MATCH (p1:Payor) WHERE p1.name = 'uhc' 
MATCH (p1)-[o:OFFERS]->(p2:Plan)-[pub:PUBLISHES]->(d:Document)-[h]->(x)
RETURN *
\"\"\"


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
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `NetworkGraph`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["NetworkGraph"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["NetworkGraph"]["events"], linkify=['Event'])







    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {};
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
