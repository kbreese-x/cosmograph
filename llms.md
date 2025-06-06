# Cosmograph

To use Cosmograph, import the Cosmograph class from @cosmograph/cosmograph and create a new instance of it with a div element and a configuration object. Then, set the data for the graph using the setData method.

```js
import { Cosmograph } from '@cosmograph/cosmograph'

const nodes = [
  { id: 0, color: 'red' },
  { id: 1, color: 'green' },
  { id: 2, color: 'blue' },
]

const links = [
  { source: 0, target: 1, color: 'blue' },
  { source: 1, target: 2, color: 'green' },
  { source: 2, target: 0, color:'red' },
]

const cosmographContainer = document.createElement('div')
const config = {
  simulation: {
    repulsion: 0.5,
  },
  renderLinks: true,
  linkColor: link => link.color,
  nodeColor: node => node.color,
  events: {
    onClick: node => {
      console.log('Clicked node: ', node)
    },
  },
  /* ... */
}

const cosmograph = new Cosmograph(canvas, config)
cosmograph.setData(nodes, links)
```

## Preparing data
Cosmograph expects the data to be nodes and links arrays:

```js
const nodes: Node[] = [...]
const links: Link[] = [...]
```

> You don't need TypeScript to use Cosmograph. But we'll still provide TypeScript types across the documentation as a reference.

Each node object needs to have a unique identifier specified in the id property. You can optionally provide starting positions for each node using the x and y properties. The links will need to have the source and target properties referencing specific nodes by their unique id.

```js
type Node = {
  id: string;
  x?: number;
  y?: number;
}

type Link = {
  source: string;
  target: string;
}
```

## Initializing the graph
After your data is ready, you can initialize Cosmograph by defining its configuration and passing the data. The way to do it will depend on whether you use React or plain JavaScript. Below you can find an example code of how you can initialize Cosmograph with a simple configuration.

> While Cosmograph doesn't have adaptors to other UI frameworks besides React, you can still integrate it into your Angular, Vue, Svelte, or other app, by using JavaScript code.

```js
import { Cosmograph } from '@cosmograph/cosmograph'

// Create an HTML element
const targetElement = document.createElement('div')
document.body.appendChild(targetElement)

// Define the configuration (CosmographInputConfig<Node, Link>)
const config = {
  nodeColor: d => d.color,
  nodeSize: 20,
  linkWidth: 2,
  // ... 
}

// Create a Cosmograph instance with the target element
const cosmograph = new Cosmograph(targetElement, config)

// Set the data
cosmograph.setData(nodes, links)
```


## Passing the data and configuration
If you use JavaScript, you can pass the data and configuration to the Cosmograph instance using the setData and setConfig methods.

```js
const config = {
  nodeColor: d => d.color,
  nodeSize: 20,
  linkWidth: 2,
}

cosmograph.setConfig(config)
cosmograph.setData(nodes, links)
```


## Events configuration
Cosmograph supports several event handlers allowing you to react to user interactions with the graph. Try clicking on a node in the example below:

### Mouse and zoom events

`onClick(clickedNode?: N, index?: number, nodePosition?: [number, number], event: MouseEvent)`
Triggered on every canvas click. If clicked on a node, its data will be passed as the first argument, index as the second argument, position as the third argument and the corresponding mouse event as the forth argument.

`onLabelClick(node: N, event: MouseEvent)`
Called when clicked on a label. The node data for this label will be passed as the first argument, and the corresponding mouse event as the second argument.

`onMouseMove(hoveredNode?: N, index?: number, nodePosition?: [number, number], event: MouseEvent) => void`
Called when mouse movement occurs. If the mouse hovers over a node, it receives the hovered node's data, index, position, and the corresponding mouse event as arguments.

`onNodeMouseOver(hoveredNode: N, index: number, nodePosition: [number, number], event?: MouseEvent | D3ZoomEvent<HTMLCanvasElement, undefined>`
Invoked when a node becomes highlighted, i.e. appears under the mouse as a result of a mouse event, zooming and panning, or movement of nodes. It receives the node's data, index, position, and the corresponding mouse event or D3 zoom event as arguments.

`onNodeMouseOut(event?: MouseEvent | D3ZoomEvent<HTMLCanvasElement, undefined>)`
Called when node is no longer underneath the mouse pointer because of a mouse event, zoom/pan event, or movement of nodes. The corresponding mouse event or D3 zoom event event will be passed as the first argument.

`onZoomStart(event: D3ZoomEvent<HTMLCanvasElement, undefined>, userDriven: boolean)`
Triggered when zooming or panning starts. It receives a D3 zoom event as the first argument and a boolean indicating whether the event was initiated by a user interaction.

`onZoom(event: D3ZoomEvent<HTMLCanvasElement, undefined>, userDriven: boolean)`
This callback function is continuously called during zooming or panning. It receives a D3 zoom event as the first argument and a boolean indicating whether the event was initiated by a user interaction.

`onZoomEnd(event: D3ZoomEvent<HTMLCanvasElement, undefined>, userDriven: boolean)`
Called when zooming or panning ends. It receives a D3 zoom event as the first argument and a boolean indicating whether the event was initiated by a user interaction.

### Simulation callbacks
Cosmograph also supports several callbacks that allow you to react to simulation events:

`onSimulationStart()`
This callback function is triggered when the simulation starts

`onSimulationTick(alpha: number, hoveredNode?: N, index?: number, nodePosition?: [number, number])`
Callback function that will be called on every simulation tick. The value of the argument alpha will decrease over time as the simulation "cools down". If there's a node under the mouse pointer, its datum will be passed as the second argument, index as the third argument and position as the forth argument.

`onSimulationEnd()`
Triggered when the simulation stops.

`onSimulationPause()`
Triggered when the simulation pauses.

`onSimulationRestart()`
Callback function that will be called when the simulation is restarted.

`onSetData(nodes: N[], links: L[])`
This callback function executes when the data of the simulation is updated. It receives two parameters: an array of nodes and an array of links. Utilize this callback to respond to changes in the data and update the visualization accordingly.

### Crossfilter callbacks

Cosomgraph has a built-in crossfilters that filters nodes and links arrays based on various selections such as Histogram, Timeline, Search or manual nodes or links selection through clicking or using the API like selectNodes. Cosmograph supports two callbacks that enable you to monitor changes in crossfilters:

`onNodesFiltered(filteredNodes?: N[])`
Triggered whenever the nodes array is filtered using node-based crossfilter.

`onLinksFiltered(filteredLinks?: L[])`
Triggered whenever the links array is filtered using link-based crossfilter.

## Controlling the graph
Cosmograph provides methods to control your graph. In JavaScript or TypeScript, you can call these methods directly on the Cosmograph instance. In React, you can access the Cosmograph instance using the useCallback or useRef hook. Here's an example of methods usage:

```js
// In JavaScript you can simply call the methods on the Cosmograph
// instance once the graph has been initialized
cosmograph.zoomToNode({ id: 'node0' })
```


### Node methods

`selectNode(node: N, selectAdjacentNodes: boolean)`
Selects a specific node. An optional boolean flag selectAdjacentNodes that is false by default can be provided to select the adjacent nodes as well.

`selectNodes(nodes: N[])`
Selects a set of nodes by passing an array of nodes as an argument.

`selectNodesInRange(selection: [[number, number], [number, number]] | null)`
Selects the nodes within a specific range. The range can be specified as a two-dimensional array of boundaries or as null to unselect all nodes.

`getSelectedNodes()`
Returns an array of nodes that are currently selected.

`unselectNodes()`
Clears the selection and unselects all nodes.

`focusNode(node?: N)`
Sets focus to a specific node by drawing a circle around it. If no node is provided, the focus is reset.

`getAdjacentNodes(id: string)`
Returns an array of adjacent nodes to a specific node by its id, or undefined.

`getNodePositions()`
Get current X and Y coordinates of all nodes. Returns an object where keys are the ids of the nodes and values are corresponding { x: number; y: number } objects.

`getNodePositionsMap()`
Get current X and Y coordinates of all nodes. Returns a Map object where keys are the ids of the nodes and values are their corresponding X and Y coordinates in the [number, number] format.

`getNodePositionsArray()`
Get current X and Y coordinates of all nodes. Returns an array of [x: number, y: number] arrays.

`getSampledNodePositionsMap()`
Gets a Map of sampled node ids to their X and Y positions for nodes currently visible on screen. The number of nodes returned depends on nodeSamplingDistance configuration property, and nodes are evenly distributed.

`getNodeDegrees()`
Returns an array of node degree values (number of connections) in the order they were sent to Cosmograph.

`getNodeRadiusByIndex(index: number)`
Get node radius by its index.

`getNodeRadiusById(id: string)`
Get node radius by its id.

`maxPointSize`
Getter. Returns a numeric value that represents the maximum point size. This value is the maximum size of the gl.POINTS primitive that WebGL can render on the user's hardware.

### Zooming

`fitView(duration = 250)`
The fitView method centers and zooms in or out the view to fit all nodes in the scene. durarion of animation for fitView() is passed in milliseconds and defaults to 250.

`fitViewByNodeIds(ids: string[], duration = 250)`
The fitViewByNodeIds method centers and zooms in or out the view to fit nodes by the list of passed ids. durarion of animation for fitView() is passed in milliseconds and defaults to 250.

`zoomToNode(node: N)`
Zooms the view to a specific node.

`setZoomLevel(value: number, duration = 0)`
Zooms the view in or out to the specified zoom level passed in value. The duration parameter specifies the duration of the zoom in/out transition and equals 0 by default.

`getZoomLevel`
Getter. Returns a numeric value that represents zoom level value of the view.

### Simulation methods

`start(alpha?: number)`
Starts the simulation. Has an optional alpha argument that is responsible for simulation impulse. The higher the alpha, the more initial energy the simulation will get. The default is 1 with a valid range between 0 and 1.

`pause()`
Pauses the simulation.

`step()`
Render only one frame of the simulation. Stops the simulation if it was running.

`restart()`
Unpauses the simulation. Unlike the start() method, restart continues the simulation from its current state without giving a start impulse.

`progress`
Getter. Returns a simulation progress value that indicates how far the simulation has progressed from the start to the end. It is a number between 0 and 1, where 0 represents the start of the simulation and 1 represents the end.

`isSimulationRunning`
Getter. Returns a boolean that indicates simulation state.

### Miscellaneous

`remove()`
Destroys the graph instance and cleans up the context.

`create()`
Create new graph instance.

`spaceToScreenPosition(spacePosition: [number, number])`
Converts the X and Y node coordinates from the space coordinate system to the screen coordinate system.

`spaceToScreenRadius(spaceRadius: number)`
Converts the node radius value from the space coordinate system to the screen coordinate system.