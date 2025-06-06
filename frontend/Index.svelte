<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import { Block, BlockLabel, Info } from "@gradio/atoms";
	import GraphIcon from "./shared/GraphIcon.svelte";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import Cosmograph from "./shared/Cosmograph.svelte";
	import type { Node, Link } from "./shared/types";

	export let value: {
		nodes: Node[];
		links: Link[];
		config: Record<string, any>;
	} | null = null;
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
	$: config = value?.config || {};
</script>

<Block {elem_id} {elem_classes} {visible} {container} {scale} {min_width}>
	<BlockLabel {show_label} Icon={GraphIcon} label={label || "Graph"} />

	<StatusTracker
		autoscroll={gradio.autoscroll}
		i18n={gradio.i18n}
		{...loading_status}
		on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
	/>

	<Cosmograph {nodes} {links} {config} />
</Block>

<style>
	:global(.cosmograph-container) {
		border-radius: var(--radius-lg);
		border: 1px solid var(--border-color-primary);
		overflow: hidden;
	}
</style>
