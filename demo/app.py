import gradio as gr
# from gradio_cosmograph import NetworkGraph


sample_data = {
    "nodes": [
        {"id": "Kai", "label": "Kai (You)", "color": "#f97316", "size": 10},
        {"id": "ChatGPT", "label": "LLM Assistant", "color": "#3b82f6", "size": 12},
        {"id": "Project", "label": "Codebot Project", "color": "#22c55e", "size": 8},
        {"id": "AWS", "label": "AWS Cloud", "color": "#facc15", "size": 8},
        {"id": "Gradio", "label": "Gradio UI", "color": "#a855f7", "size": 9},
        {"id": "Cosmograph", "label": "GPU Graph Lib", "color": "#ec4899", "size": 9},
        {"id": "LangChain", "label": "LangChain", "color": "#0ea5e9", "size": 7},
        {"id": "S3", "label": "S3 Bucket", "color": "#ef4444", "size": 7},
        {"id": "Lambda", "label": "AWS Lambda", "color": "#14b8a6", "size": 7},
        {"id": "SageMaker", "label": "SageMaker Endpt.", "color": "#64748b", "size": 7},
        {"id": "Alice", "label": "Random User A", "color": "#fb923c", "size": 6},
        {"id": "Bob", "label": "Random User B", "color": "#60a5fa", "size": 6},
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

with gr.Blocks() as demo:
    gr.Markdown(
        "# Change the value (keep it JSON) and the front-end will update automatically."
    )
    gr.JSON(value=sample_data)
    # NetworkGraph(value=sample_data, label="Static")


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")
