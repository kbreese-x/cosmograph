<script lang="ts">
import { onMount, onDestroy, afterUpdate } from 'svelte';
import { Cosmograph } from '@cosmograph/cosmograph';
import type { Node, Link } from '../shared/types';

export let nodes: Node[] = [];
export let links: Link[] = [];
export let config: Record<string, any> = {};

let container: HTMLDivElement;
let cosmograph: Cosmograph<Node, Link> | undefined;

onMount(() => {
  if (!container) return;
  
  cosmograph = new Cosmograph(container, config);
  cosmograph.setData(nodes, links);
});

afterUpdate(() => {
  if (!cosmograph) return;

  // Update data when props change
  cosmograph.setData(nodes, links);
  
  // Update config when it changes
  cosmograph.setConfig(config);
});

onDestroy(() => {
  if (cosmograph) {
    cosmograph.remove();
  }
});
</script>

<div 
  bind:this={container} 
  class="cosmograph-container"
>
</div>

<style>
.cosmograph-container {
  width: 100%;
  height: 100%;
  min-height: 400px;
  position: relative;
}
</style>