​BFS + Greedy Dijkstra
1. Similar to the previous approach, we first need to populate the grid with the safeness values for each cell. The algorithm to achieve this is the same as before, using the breadth-first Search (BFS) technique to compute the distance of each cell from the nearest thief. The commplexity is O(n^2) since every cell is visited exactly once - brute force of checking each cell against thief would be O(n^4).
2. The key idea here is to use Dijkstra's single source shortest path algorithm to find the optimal path from the source cell `[0, 0]` to the destination cell `[n-1, n-1]`. However, since each cell in the grid already contains its safeness factor, we need to modify Dijkstra's algorithm to find the path with the maximum safeness factor. In our modified Dijkstra's algorithm, we can greedily prioritize cells with a higher safeness factor to append to our path. The safeness factor of the path would be the minimum of the safeness values encountered in that path so far. Once we reach the destination cell, the safeness factor of the path would represent the required maximum safeness factor.

Small comments 
- Use -1 to mark unvisited grid for `multi_source_queue` algorithm, but use -1 to mark visited path cell.
- In the Dijkstra's while loop, iterate on the saved new variable size instead of the length of priority queue, since we need the flexibility to make changes to the queue.