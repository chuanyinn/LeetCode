Initially I tried to have the helper function return boolean of yes/no good node, but keeping track of counts is better. Depth-First Search (DFS) recursion with helper function `dfs`.
1. ​Depth-First Search (DFS): Perform a DFS traversal of the tree. This will allow us to keep track of the path we are taking.
2. Track Maximum Value: As we traverse, keep track of the maximum value encountered along the path.
3. Count Good Nodes: For each node, compare its value to the maximum value tracked so far. If the node's value is greater than or equal to the maximum value, it is a "good" node. Update the maximum value as needed.
