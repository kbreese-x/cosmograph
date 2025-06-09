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

	export let value: {
		nodes: Node[];
		links: Link[];
	} | null = null;

	export let background_color: string | undefined = undefined;
	export let node_size_scale: number | undefined = undefined;
	export let link_width_scale: number | undefined = undefined;
	export let disable_zoom = false;
	export let show_hovered_node_label = false;
	export let disable_simulation = false;
	export let gravity: number | undefined = undefined;
	export let repulsion: number | undefined = undefined;

	export let label = "Graph";
	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let loading_status: LoadingStatus;
	export let show_label = true;
	export let container = true;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let gradio: Gradio<{
		change: never;
		clear_status: LoadingStatus;
	}>;

	$: nodes = value?.nodes || [];
	$: links = value?.links || [];
	$: graphConfig = createConfig({
		backgroundColor: background_color,
		nodeSizeScale: node_size_scale,
		linkWidthScale: link_width_scale,
		disableZoom: disable_zoom,
		showHoveredNodeLabel: show_hovered_node_label,
		disableSimulation: disable_simulation,
		gravity,
		repulsion,
	});
</script>

<Block {elem_id} {elem_classes} {visible} {container} {scale} {min_width}>
	<BlockLabel {show_label} Icon={GraphIcon} label={label || "Graph"} />

	<StatusTracker
		autoscroll={gradio.autoscroll}
		i18n={gradio.i18n}
		{...loading_status}
		on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
	/>

	<Cosmograph {nodes} {links} config={graphConfig} />
</Block>
