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
        scale_nodes_on_zoom: bool = True,
        pixel_ratio: float = 2.0,
        # Node appearance
        node_greyout_opacity: float = 0.1,
        focused_node_ring_color: str = "white",
        render_hovered_node_ring: bool = True,
        hovered_node_ring_color: str = "white",
        # Link appearance
        render_links: bool = True,
        link_arrows: bool = True,
        link_arrows_size_scale: float = 1.0,
        link_greyout_opacity: float = 0.1,
        curved_links: bool = False,
        curved_link_segments: int = 19,
        curved_link_weight: float = 0.8,
        curved_link_control_point_distance: float = 0.5,
        link_visibility_min_transparency: float = 0.25,
        link_visibility_distance_range: tuple[float, float] = (50, 150),
        # Label configuration
        node_label_key: str = "id",
        show_dynamic_labels: bool = True,
        show_top_labels: bool = True,
        show_top_labels_limit: int = 100,
        show_hovered_node_label: bool = True,
        # Interaction settings
        disable_zoom: bool = False,
        initial_zoom_level: float = 1.0,
        fit_view_on_init: bool = True,
        fit_view_delay: int = 250,
        # Simulation parameters
        disable_simulation: bool = False,
        space_size: int = 4096,
        simulation_decay: int = 1000,
        simulation_friction: float = 0.85,
        simulation_repulsion: float = 0.1,
        simulation_repulsion_theta: float = 1.7,
        simulation_link_spring: float = 1.0,
        simulation_link_distance: float = 2.0,
        simulation_gravity: float = 0.0,
        simulation_center: float = 0.0,
        simulation_repulsion_from_mouse: float = 2.0,
        use_quadtree: bool = False,
        repulsion_quadtree_levels: int = 12,
        # Standard Gradio parameters
        label: str | I18nData | None = None,
        info: str | I18nData | None = None,
        every: float | None = None,
        inputs: Component | Sequence[Component] | set[Component] | None = None,
        show_label: bool = True,
        container: bool = True,
        scale: int | None = None,
        min_width: int = 160,
        min_height: int = 160,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        key: int | str | tuple[int | str, ...] | None = None,
        preserved_by_key: list[str] | str | None = "value",
    ):
        """
        Creates a network graph visualization component using Cosmograph.

        Parameters:
            value: A dictionary containing the graph data with 'nodes' and 'links' lists. Each node should have an 'id' property
                and optionally 'color' and 'size'. Each link should have 'source' and 'target' properties referencing node IDs.

        Visual Configuration:
            background_color: The color of the graph background. Accepts any valid CSS color string.
            node_size_scale: Scale factor for all node sizes. Default is 1.0.
            link_width_scale: Scale factor for all link widths. Default is 1.0.
            scale_nodes_on_zoom: Whether nodes should scale when zooming. Default is True.
            pixel_ratio: Canvas pixel ratio for rendering quality. Default is 2.0.

        Node Appearance:
            node_greyout_opacity: Opacity of unselected nodes when selection is active (0-1). Default is 0.1.
            focused_node_ring_color: Color of the ring around focused nodes. Default is "white".
            render_hovered_node_ring: Whether to show a ring around hovered nodes. Default is True.
            hovered_node_ring_color: Color of the ring around hovered nodes. Default is "white".

        Link Appearance:
            render_links: Whether to render links between nodes. Default is True.
            link_arrows: Whether to show arrows on links. Default is True.
            link_arrows_size_scale: Scale factor for link arrow size. Default is 1.0.
            link_greyout_opacity: Opacity of unselected links when selection is active (0-1). Default is 0.1.
            curved_links: Whether to render curved links. Default is False.
            curved_link_segments: Number of segments in curved links. Default is 19.
            curved_link_weight: Weight factor for curve shape (0-1). Default is 0.8.
            curved_link_control_point_distance: Distance of curve control point. Default is 0.5.
            link_visibility_min_transparency: Minimum transparency for long links. Default is 0.25.
            link_visibility_distance_range: Range for link length-based transparency (min, max). Default is (50, 150).

        Label Configuration:
            node_label_key: Key from node data to use as label text. Default is "id".
            show_dynamic_labels: Whether to show labels while zooming. Default is True.
            show_top_labels: Whether to show labels for top nodes. Default is False.
            show_top_labels_limit: Maximum number of top labels to show. Default is 100.
            show_hovered_node_label: Whether to show label for hovered node. Default is True.

        Interaction Settings:
            disable_zoom: If True, prevents zooming and panning. Default is False.
            initial_zoom_level: Starting zoom level. Default is 1.0.
            fit_view_on_init: Whether to fit view to all nodes on init. Default is True.
            fit_view_delay: Delay before fitting view on init (ms). Default is 250.

        Simulation Parameters:
            disable_simulation: If True, nodes won't move after placement. Default is False.
            space_size: Size of simulation space (max 8192). Default is 4096.
            simulation_decay: Force simulation decay coefficient. Default is 1000.
            simulation_friction: Friction coefficient (0.8-1.0). Default is 0.85.
            simulation_repulsion: Node repulsion force (0.0-2.0). Default is 0.1.
            simulation_repulsion_theta: Barnes-Hut approximation criterion (0.3-2.0). Default is 1.7.
            simulation_link_spring: Link spring force (0.0-2.0). Default is 1.0.
            simulation_link_distance: Minimum distance between linked nodes. Default is 2.0.
            simulation_gravity: Gravity force toward center (0.0-1.0). Default is 0.0.
            simulation_center: Centering force (0.0-1.0). Default is 0.0.
            simulation_repulsion_from_mouse: Mouse repulsion force (0.0-5.0). Default is 2.0.
            use_quadtree: Whether to use quadtree algorithm. Default is False.
            repulsion_quadtree_levels: Depth of quadtree approximation. Default is 12.

        Standard Gradio Parameters:
            label: Component label shown in UI.
            info: Tooltip information text.
            every: Number of seconds between value updates.
            inputs: Components that trigger value updates.
            show_label: Whether to show the component label.
            container: Whether to use container styling.
            scale: Relative width compared to other components.
            min_width: Minimum pixel width.
            visible: Whether component is visible.
            elem_id: HTML element ID.
            elem_classes: HTML element classes.
            render: Whether to render in Blocks context.
            key: Unique key for component identity across renders.
            preserved_by_key: Parameters to preserve across re-renders.
        """
        self.background_color = background_color
        self.node_size_scale = node_size_scale
        self.link_width_scale = link_width_scale
        self.scale_nodes_on_zoom = scale_nodes_on_zoom
        self.pixel_ratio = pixel_ratio

        self.node_greyout_opacity = node_greyout_opacity
        self.focused_node_ring_color = focused_node_ring_color
        self.render_hovered_node_ring = render_hovered_node_ring
        self.hovered_node_ring_color = hovered_node_ring_color

        self.render_links = render_links
        self.link_arrows = link_arrows
        self.link_arrows_size_scale = link_arrows_size_scale
        self.link_greyout_opacity = link_greyout_opacity
        self.curved_links = curved_links
        self.curved_link_segments = curved_link_segments
        self.curved_link_weight = curved_link_weight
        self.curved_link_control_point_distance = curved_link_control_point_distance
        self.link_visibility_min_transparency = link_visibility_min_transparency
        self.link_visibility_distance_range = link_visibility_distance_range

        self.node_label_key = node_label_key
        self.show_dynamic_labels = show_dynamic_labels
        self.show_top_labels = show_top_labels
        self.show_top_labels_limit = show_top_labels_limit
        self.show_hovered_node_label = show_hovered_node_label

        self.disable_zoom = disable_zoom
        self.initial_zoom_level = initial_zoom_level
        self.fit_view_on_init = fit_view_on_init
        self.fit_view_delay = fit_view_delay

        self.disable_simulation = disable_simulation
        self.space_size = space_size
        self.simulation_decay = simulation_decay
        self.simulation_friction = simulation_friction
        self.simulation_repulsion = simulation_repulsion
        self.simulation_repulsion_theta = simulation_repulsion_theta
        self.simulation_link_spring = simulation_link_spring
        self.simulation_link_distance = simulation_link_distance
        self.simulation_gravity = simulation_gravity
        self.simulation_center = simulation_center
        self.simulation_repulsion_from_mouse = simulation_repulsion_from_mouse
        self.use_quadtree = use_quadtree
        self.repulsion_quadtree_levels = repulsion_quadtree_levels

        self.min_height = min_height

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
