import shutil
import subprocess
from pathlib import Path
import gradio 

component_directory = Path(".").resolve()
print(f"COMPONENT_DIRECTORY={component_directory}")

node = shutil.which("node")
if not node:
    raise ValueError(
        "node must be installed in order to run build command."
    )

gradio_node_path = subprocess.run(
    [node, "-e", "console.log(require.resolve('@gradio/preview'))"],
    cwd=Path(component_directory / "frontend"),
    check=False,
    capture_output=True,
)

if gradio_node_path.returncode != 0:
    raise ValueError(
        "Could not find `@gradio/preview`. Run `npm i -D @gradio/preview` in your frontend folder."
    )

gradio_node_path = gradio_node_path.stdout.decode("utf-8").strip()
print(f"GRADIO_NODE_PATH={gradio_node_path}")

gradio_template_path = Path(gradio.__file__).parent / "templates" / "frontend"
print(f"GRADIO_TEMPLATE_PATH={gradio_template_path}")