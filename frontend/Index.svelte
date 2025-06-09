<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import { Block, BlockLabel, Info } from "@gradio/atoms";
	import GraphIcon from "./shared/GraphIcon.svelte";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import Cosmograph from "./shared/Cosmograph.svelte";
	import type { Node, Link } from "./shared/types";
	import type { GraphProps } from "./shared/cosmographConfig";
	import { createConfig } from "./shared/cosmographConfig";
	import "./shared/global.css";

	// Index.svelte export statements
	export let value: {
		nodes: Node[];
		links: Link[];
	} | null = null;

	// Visual configuration
	export let background_color: string | undefined = undefined;
	export let node_size_scale = 1.0;
	export let link_width_scale = 1.0;
	export let scale_nodes_on_zoom = true;
	export let pixel_ratio = 2.0;

	// Node appearance
	export let node_greyout_opacity = 0.1;
	export let focused_node_ring_color = "white";
	export let render_hovered_node_ring = true;
	export let hovered_node_ring_color = "white";

	// Link appearance
	export let render_links = true;
	export let link_arrows = true;
	export let link_arrows_size_scale = 1.0;
	export let link_greyout_opacity = 0.1;
	export let curved_links = false;
	export let curved_link_segments = 19;
	export let curved_link_weight = 0.8;
	export let curved_link_control_point_distance = 0.5;
	export let link_visibility_min_transparency = 0.25;
	export let link_visibility_distance_range: [number, number] = [50, 150];

	// Label configuration
	export let node_label_key = "id";
	export let show_dynamic_labels = true;
	export let show_top_labels = false;
	export let show_top_labels_limit = 100;
	export let show_hovered_node_label = true;

	// Interaction settings
	export let disable_zoom = false;
	export let initial_zoom_level = 1.0;
	export let fit_view_on_init = true;
	export let fit_view_delay = 250;

	// Simulation parameters
	export let disable_simulation = false;
	export let space_size = 4096;
	export let simulation_decay = 1000;
	export let simulation_friction = 0.85;
	export let simulation_repulsion = 0.1;
	export let simulation_repulsion_theta = 1.7;
	export let simulation_link_spring = 1.0;
	export let simulation_link_distance = 2.0;
	export let simulation_gravity = 0.0;
	export let simulation_center = 0.0;
	export let simulation_repulsion_from_mouse = 2.0;
	export let use_quadtree = false;
	export let repulsion_quadtree_levels = 12;

	// Standard Gradio parameters
	export let label = "Graph";
	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let loading_status: LoadingStatus;
	export let show_label = true;
	export let container = true;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let min_height: number | undefined = undefined;
	export let gradio: Gradio<{
		change: never;
		clear_status: LoadingStatus;
	}>;

	$: nodes = value?.nodes || [];
	$: links = value?.links || [];
	$: graphConfig = createConfig({
		// Visual configuration
		backgroundColor: background_color,
		nodeSizeScale: node_size_scale,
		linkWidthScale: link_width_scale,
		scaleNodesOnZoom: scale_nodes_on_zoom,
		pixelRatio: pixel_ratio,

		// Node appearance
		nodeGreyoutOpacity: node_greyout_opacity,
		focusedNodeRingColor: focused_node_ring_color,
		renderHoveredNodeRing: render_hovered_node_ring,
		hoveredNodeRingColor: hovered_node_ring_color,

		// Link appearance
		renderLinks: render_links,
		linkArrows: link_arrows,
		linkArrowsSizeScale: link_arrows_size_scale,
		linkGreyoutOpacity: link_greyout_opacity,
		curvedLinks: curved_links,
		curvedLinkSegments: curved_link_segments,
		curvedLinkWeight: curved_link_weight,
		curvedLinkControlPointDistance: curved_link_control_point_distance,
		linkVisibilityMinTransparency: link_visibility_min_transparency,
		linkVisibilityDistanceRange: link_visibility_distance_range,

		// Label configuration
		nodeLabelKey: node_label_key,
		showDynamicLabels: show_dynamic_labels,
		showTopLabels: show_top_labels,
		showTopLabelsLimit: show_top_labels_limit,
		showHoveredNodeLabel: show_hovered_node_label,

		// Interaction settings
		disableZoom: disable_zoom,
		initialZoomLevel: initial_zoom_level,
		fitViewOnInit: fit_view_on_init,
		fitViewDelay: fit_view_delay,

		// Simulation settings
		disableSimulation: disable_simulation,
		spaceSize: space_size,
		simulationDecay: simulation_decay,
		simulationFriction: simulation_friction,
		simulationRepulsion: simulation_repulsion,
		simulationRepulsionTheta: simulation_repulsion_theta,
		simulationLinkSpring: simulation_link_spring,
		simulationLinkDistance: simulation_link_distance,
		simulationGravity: simulation_gravity,
		simulationCenter: simulation_center,
		simulationRepulsionFromMouse: simulation_repulsion_from_mouse,
		useQuadtree: use_quadtree,
		repulsionQuadtreeLevels: repulsion_quadtree_levels,
	});
</script>

<Block {elem_id} {elem_classes} {visible} {container} {scale} {min_width} {min_height}>
	<BlockLabel {show_label} Icon={GraphIcon} label={label || "Graph"} />

	<StatusTracker
		autoscroll={gradio.autoscroll}
		i18n={gradio.i18n}
		{...loading_status}
		on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
	/>

	<Cosmograph {nodes} {links} config={graphConfig} />
</Block>
