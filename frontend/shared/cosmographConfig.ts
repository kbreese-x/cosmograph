import type { CosmographConfigInterface, CosmosInputNode, CosmosInputLink } from '@cosmograph/cosmograph';
import type { Node, Link } from './types';

// Base default configuration that will be merged with user options
export const defaultConfig: Partial<CosmographConfigInterface<Node, Link>> = {
  // Visual defaults
  backgroundColor: '#ffffff',
  nodeColor: (node) => node.color || '#b3b3b3',
  nodeSize: (node) => node.size || 4,
  nodeSizeScale: 1,
  
  // Link styling
  renderLinks: true,
  linkColor: (link) => link.color || '#666666',
  linkWidth: (link) => link.width || 1,
  linkWidthScale: 1,
  
  // Interaction settings
  renderHoveredNodeRing: true,
  hoveredNodeRingColor: '#000000',
  scaleNodesOnZoom: true,
  
  // Simulation settings
  simulationDecay: 1000,
  simulationGravity: 0.1,
  simulationRepulsion: 0.1,
  simulationLinkSpring: 1,
  simulationFriction: 0.85,
  
  // View settings
  fitViewOnInit: true,
  fitViewDelay: 250,
};

// Props that can be passed to Index.svelte to control graph behavior
export interface GraphProps {
  // Core display
  backgroundColor?: string;
  nodeSizeScale?: number;
  linkWidthScale?: number;
  
  // Interaction
  disableZoom?: boolean;
  showHoveredNodeLabel?: boolean;
  
  // Simulation
  disableSimulation?: boolean;
  gravity?: number;
  repulsion?: number;
  
  // Events
  onNodeClick?: (node: Node) => void;
  onNodeHover?: (node: Node | undefined) => void;
}

// Function to merge default config with user props
export function createConfig(props: GraphProps): CosmographConfigInterface<Node, Link> {
  return {
    ...defaultConfig,
    backgroundColor: props.backgroundColor ?? defaultConfig.backgroundColor,
    nodeSizeScale: props.nodeSizeScale ?? defaultConfig.nodeSizeScale,
    linkWidthScale: props.linkWidthScale ?? defaultConfig.linkWidthScale,
    disableZoom: props.disableZoom ?? false,
    showHoveredNodeLabel: props.showHoveredNodeLabel ?? false,
    disableSimulation: props.disableSimulation ?? false,
    simulationGravity: props.gravity ?? defaultConfig.simulationGravity,
    simulationRepulsion: props.repulsion ?? defaultConfig.simulationRepulsion,
    events: {
      onClick: props.onNodeClick ? (node) => node && props.onNodeClick!(node as Node) : undefined,
      onNodeMouseOver: props.onNodeHover ? (node) => props.onNodeHover!(node as Node) : undefined,
      onNodeMouseOut: props.onNodeHover ? () => props.onNodeHover!(undefined) : undefined,
    }
  } as CosmographConfigInterface<Node, Link>;
}