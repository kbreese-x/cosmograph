<script lang="ts">
  import { onMount, onDestroy, afterUpdate } from "svelte";
  import { Cosmograph } from "@cosmograph/cosmograph";
  import type { CosmographConfigInterface } from "@cosmograph/cosmograph";
  import type { Node, Link } from "../shared/types";
  import { defaultConfig } from "./cosmographConfig";

  export let nodes: Node[] = [];
  export let links: Link[] = [];
  export let config: Partial<CosmographConfigInterface<Node, Link>> = {};
  let container: HTMLDivElement;
  let cosmograph: Cosmograph<Node, Link> | undefined;

  onMount(() => {
    if (!container) return;

    const mergedConfig = {
      ...defaultConfig,
      ...config,
    } as CosmographConfigInterface<Node, Link>;
    cosmograph = new Cosmograph(container, mergedConfig);
    cosmograph.setData(nodes, links);
  });

  afterUpdate(() => {
    if (!cosmograph) return;

    cosmograph.setData(nodes, links);

    cosmograph.setConfig({
      ...defaultConfig,
      ...config,
    } as CosmographConfigInterface<Node, Link>);
  });

  onDestroy(() => {
    if (cosmograph) {
      cosmograph.remove();
    }
  });
</script>

<div bind:this={container} class="cosmograph-container"></div>

<style>
  .cosmograph-container {
    width: 100%;
    height: 100%;
    /* min-height: 400px; */
    position: relative;
  }
</style>
