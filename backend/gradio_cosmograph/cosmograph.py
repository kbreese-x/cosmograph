from __future__ import annotations

from collections.abc import Sequence
from typing import Any, Callable

from gradio.components.base import Component
from gradio.events import Events
from gradio.i18n import I18nData

class NetworkGraph(Component):
    """
    Creates a network graph visualization component using Cosmograph. Can be used to display node-link diagrams
    with customizable styling and interaction options.
    """

    EVENTS = [Events.change]

    def __init__(
        self,
        value: dict[str, Any] | None = None,
        *,
        # Visual configuration
        background_color: str | None = None,
        node_size_scale: float = 1.0,
        link_width_scale: float = 1.0,
        
        # Interaction settings
        disable_zoom: bool = False,
        show_hovered_node_label: bool = False,
        
        # Simulation parameters
        disable_simulation: bool = False,
        gravity: float = 0.1,
        repulsion: float = 0.1,
        
        # Standard Gradio parameters
        label: str | I18nData | None = None,
        info: str | I18nData | None = None,
        every: float | None = None,
        inputs: Component | Sequence[Component] | set[Component] | None = None,
        show_label: bool = True,
        container: bool = True,
        scale: int | None = None,
        min_width: int = 160,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        key: int | str | tuple[int | str, ...] | None = None,
        preserved_by_key: list[str] | str | None = "value",
    ):
        """
        Parameters:
            value: A dictionary containing the graph data with 'nodes' and 'links' lists. Each node should have an 'id' property
                  and optionally 'color' and 'size'. Each link should have 'source' and 'target' properties referencing node IDs.
                  If a function is provided, it will be called each time the app loads to set the initial value.
            background_color: The color of the graph background. Accepts any valid CSS color string.
            node_size_scale: Scale factor for all node sizes. Default is 1.0.
            link_width_scale: Scale factor for all link widths. Default is 1.0.
            disable_zoom: If True, prevents zooming and panning of the graph. Default is False.
            show_hovered_node_label: If True, displays a label when hovering over nodes. Default is False.
            disable_simulation: If True, nodes will not move after initial placement. Default is False.
            gravity: Strength of the gravity force pulling nodes toward the center. Range [0, 1], default 0.1.
            repulsion: Strength of the repulsive force between nodes. Range [0, 1], default 0.1.
            label: The label for this component. Appears above the component and is also used as the header if there are 
                  examples for this component.
            info: Additional information about the component to be displayed to the user as a tooltip.
            every: Number of seconds to wait between refreshing the component. If value is a function,
                  the function will be called every `every` seconds to update the value.
            inputs: List of components that will trigger the `value` function when their values change.
            show_label: If True, will display label.
            container: If True, will place the component in a container with some padding.
            scale: Relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, 
                  and Component B has scale=1, A will be twice as wide as B.
            min_width: Minimum pixel width of the component.
            visible: If False, component will be hidden.
            elem_id: HTML element id for the component.
            elem_classes: HTML classes to add to the component.
            render: If False, component will not be rendered in the Blocks context.
            key: In gr.render, components with same key across re-renders are treated as the same component.
            preserved_by_key: Parameters to preserve across re-renders when using the same key.
        """
        self.background_color = background_color
        self.node_size_scale = node_size_scale
        self.link_width_scale = link_width_scale
        self.disable_zoom = disable_zoom
        self.show_hovered_node_label = show_hovered_node_label
        self.disable_simulation = disable_simulation
        self.gravity = gravity
        self.repulsion = repulsion

        super().__init__(
            label=label,
            info=info,
            every=every,
            inputs=inputs,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
            key=key,
            preserved_by_key=preserved_by_key,
            value=value,
        )

    def preprocess(self, payload):
        """
        This docstring is used to generate the docs for this custom component.
        Parameters:
            payload: the data to be preprocessed, sent from the frontend
        Returns:
            the data after preprocessing, sent to the user's function in the backend
        """
        return payload

    def postprocess(self, value):
        """
        This docstring is used to generate the docs for this custom component.
        Parameters:
            payload: the data to be postprocessed, sent from the user's function in the backend
        Returns:
            the data after postprocessing, sent to the frontend
        """
        return value

    def example_payload(self):
        return {"foo": "bar"}

    def example_value(self):
        return {"foo": "bar"}

    def api_info(self):
        return {"type": {}, "description": "any valid json"}
