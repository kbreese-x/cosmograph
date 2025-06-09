import type { CosmographConfigInterface } from '@cosmograph/cosmograph';
import type { Node, Link } from './types';

// Base default configuration that will be merged with user options
export const defaultConfig: Partial<CosmographConfigInterface<Node, Link>> = {
  // Visual configuration
  backgroundColor: '#ffffff',
  nodeColor: (node) => node.color || '#b3b3b3',
  nodeSize: (node) => node.size || 4,
  nodeSizeScale: 1.0,
  scaleNodesOnZoom: true,
  pixelRatio: 2.0,

  // Node appearance
  nodeGreyoutOpacity: 0.1,
  focusedNodeRingColor: 'white',
  renderHoveredNodeRing: true,
  hoveredNodeRingColor: 'white',

  // Link styling
  renderLinks: true,
  linkColor: (link) => link.color || '#666666',
  linkWidth: (link) => link.width || 1,
  linkWidthScale: 1.0,
  linkArrows: true,
  linkArrowsSizeScale: 1.0,
  linkGreyoutOpacity: 0.1,
  curvedLinks: false,
  curvedLinkSegments: 19,
  curvedLinkWeight: 0.8,
  curvedLinkControlPointDistance: 0.5,
  linkVisibilityMinTransparency: 0.25,
  linkVisibilityDistance: [50, 150],

  // Label configuration
  nodeLabelAccessor: (node) => node.id,
  showDynamicLabels: true,
  showTopLabels: false,
  showTopLabelsLimit: 100,
  showHoveredNodeLabel: true,

  // View settings
  disableZoom: false,
  initialZoomLevel: 1.0,
  fitViewOnInit: true,
  fitViewDelay: 250,

  // Simulation settings
  disableSimulation: false,
  spaceSize: 4096,
  simulationDecay: 1000,
  simulationFriction: 0.85,
  simulationRepulsion: 0.1,
  simulationRepulsionTheta: 1.7,
  simulationLinkSpring: 1.0,
  simulationLinkDistance: 2.0,
  simulationGravity: 0.0,
  simulationCenter: 0.0,
  simulationRepulsionFromMouse: 2.0,
  useQuadtree: false,
  repulsionQuadtreeLevels: 12,
};

// Props interface for the graph component
export interface GraphProps {
  // Visual configuration
  backgroundColor?: string;
  nodeSizeScale?: number;
  linkWidthScale?: number;
  scaleNodesOnZoom?: boolean;
  pixelRatio?: number;

  // Node appearance
  nodeGreyoutOpacity?: number;
  focusedNodeRingColor?: string;
  renderHoveredNodeRing?: boolean;
  hoveredNodeRingColor?: string;

  // Link appearance
  renderLinks?: boolean;
  linkArrows?: boolean;
  linkArrowsSizeScale?: number;
  linkGreyoutOpacity?: number;
  curvedLinks?: boolean;
  curvedLinkSegments?: number;
  curvedLinkWeight?: number;
  curvedLinkControlPointDistance?: number;
  linkVisibilityMinTransparency?: number;
  linkVisibilityDistanceRange?: [number, number];

  // Label configuration
  nodeLabelKey?: string;
  showDynamicLabels?: boolean;
  showTopLabels?: boolean;
  showTopLabelsLimit?: number;
  showHoveredNodeLabel?: boolean;

  // Interaction settings
  disableZoom?: boolean;
  initialZoomLevel?: number;
  fitViewOnInit?: boolean;
  fitViewDelay?: number;

  // Simulation settings
  disableSimulation?: boolean;
  spaceSize?: number;
  simulationDecay?: number;
  simulationFriction?: number;
  simulationRepulsion?: number;
  simulationRepulsionTheta?: number;
  simulationLinkSpring?: number;
  simulationLinkDistance?: number;
  simulationGravity?: number;
  simulationCenter?: number;
  simulationRepulsionFromMouse?: number;
  useQuadtree?: boolean;
  repulsionQuadtreeLevels?: number;
}

// Function to merge default config with user props
export function createConfig(props: GraphProps): CosmographConfigInterface<Node, Link> {
  return {
    ...defaultConfig,
    backgroundColor: props.backgroundColor ?? defaultConfig.backgroundColor,
    nodeSizeScale: props.nodeSizeScale ?? defaultConfig.nodeSizeScale,
    linkWidthScale: props.linkWidthScale ?? defaultConfig.linkWidthScale,
    scaleNodesOnZoom: props.scaleNodesOnZoom ?? defaultConfig.scaleNodesOnZoom,
    pixelRatio: props.pixelRatio ?? defaultConfig.pixelRatio,

    nodeGreyoutOpacity: props.nodeGreyoutOpacity ?? defaultConfig.nodeGreyoutOpacity,
    focusedNodeRingColor: props.focusedNodeRingColor ?? defaultConfig.focusedNodeRingColor,
    renderHoveredNodeRing: props.renderHoveredNodeRing ?? defaultConfig.renderHoveredNodeRing,
    hoveredNodeRingColor: props.hoveredNodeRingColor ?? defaultConfig.hoveredNodeRingColor,

    renderLinks: props.renderLinks ?? defaultConfig.renderLinks,
    linkArrows: props.linkArrows ?? defaultConfig.linkArrows,
    linkArrowsSizeScale: props.linkArrowsSizeScale ?? defaultConfig.linkArrowsSizeScale,
    linkGreyoutOpacity: props.linkGreyoutOpacity ?? defaultConfig.linkGreyoutOpacity,
    curvedLinks: props.curvedLinks ?? defaultConfig.curvedLinks,
    curvedLinkSegments: props.curvedLinkSegments ?? defaultConfig.curvedLinkSegments,
    curvedLinkWeight: props.curvedLinkWeight ?? defaultConfig.curvedLinkWeight,
    curvedLinkControlPointDistance: props.curvedLinkControlPointDistance ?? defaultConfig.curvedLinkControlPointDistance,
    linkVisibilityMinTransparency: props.linkVisibilityMinTransparency ?? defaultConfig.linkVisibilityMinTransparency,
    linkVisibilityDistance: props.linkVisibilityDistanceRange ?? defaultConfig.linkVisibilityDistance,

    nodeLabelAccessor: props.nodeLabelKey
      ? (node: Node) => node[props.nodeLabelKey as keyof Node]?.toString() ?? node.id
      : defaultConfig.nodeLabelAccessor,
    showDynamicLabels: props.showDynamicLabels ?? defaultConfig.showDynamicLabels,
    showTopLabels: props.showTopLabels ?? defaultConfig.showTopLabels,
    showTopLabelsLimit: props.showTopLabelsLimit ?? defaultConfig.showTopLabelsLimit,
    showHoveredNodeLabel: props.showHoveredNodeLabel ?? defaultConfig.showHoveredNodeLabel,

    disableZoom: props.disableZoom ?? defaultConfig.disableZoom,
    initialZoomLevel: props.initialZoomLevel ?? defaultConfig.initialZoomLevel,
    fitViewOnInit: props.fitViewOnInit ?? defaultConfig.fitViewOnInit,
    fitViewDelay: props.fitViewDelay ?? defaultConfig.fitViewDelay,

    disableSimulation: props.disableSimulation ?? defaultConfig.disableSimulation,
    spaceSize: props.spaceSize ?? defaultConfig.spaceSize,
    simulationDecay: props.simulationDecay ?? defaultConfig.simulationDecay,
    simulationFriction: props.simulationFriction ?? defaultConfig.simulationFriction,
    simulationRepulsion: props.simulationRepulsion ?? defaultConfig.simulationRepulsion,
    simulationRepulsionTheta: props.simulationRepulsionTheta ?? defaultConfig.simulationRepulsionTheta,
    simulationLinkSpring: props.simulationLinkSpring ?? defaultConfig.simulationLinkSpring,
    simulationLinkDistance: props.simulationLinkDistance ?? defaultConfig.simulationLinkDistance,
    simulationGravity: props.simulationGravity ?? defaultConfig.simulationGravity,
    simulationCenter: props.simulationCenter ?? defaultConfig.simulationCenter,
    simulationRepulsionFromMouse: props.simulationRepulsionFromMouse ?? defaultConfig.simulationRepulsionFromMouse,
    useQuadtree: props.useQuadtree ?? defaultConfig.useQuadtree,
    repulsionQuadtreeLevels: props.repulsionQuadtreeLevels ?? defaultConfig.repulsionQuadtreeLevels,
  } as CosmographConfigInterface<Node, Link>;
}