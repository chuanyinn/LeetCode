1. bfs algorithm, `defaultdict(set)` for adjacency graph, queue for leaves.
2. ​This implementation uses a breadth-first search approach to iteratively remove leaf nodes (nodes with only one neighbor) until we're left with the roots, which are the minimum height trees.
3. From each leaf in the queue, find each neighbor and delete the leaf from the adjacency set. When only left with two leaves in the queue, whatever in the leaves queue are the nodes.
