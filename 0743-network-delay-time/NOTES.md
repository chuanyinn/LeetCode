Directed graph, naturally Dijkstra's algorithm. Otherwise for loop would not cover all cases, and simple while loop can get stuck in cyclic path. This approach uses a for loop in a while loop, where the while goes over the heapq, and for loop goes over all the neighbor a node has. It's intuitively traversing from the starting node, one neighbor at a time. I think the distance should be the first argument because of priority quee?

To solve this problem, you can use Dijkstra's algorithm, which is efficient for finding the shortest path in graphs with non-negative weights. Here's a step-by-step approach to implementing the solution:

1. Represent the Graph: Use an adjacency list to represent the graph.
1. Priority Queue: Use a min-heap (priority queue) to always expand the node with the smallest known distance.
1. Distance Table: Maintain a table to store the minimum distance from the starting node `k` to every other node.
1. Dijkstra's Algorithm: Apply Dijkstra's algorithm to find the shortest path from node `k` to all other nodes.
​
