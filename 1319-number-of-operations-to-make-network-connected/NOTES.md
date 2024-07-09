Logical error - Incorrect Handling of Connections: The code is not correctly tracking the connected components. The visited set only tracks if individual nodes have been visited but does not account for the actual connections between nodes and which nodes are in the same connected component.

​UnionFind Class: Helps to efficiently manage and merge connected components.

makeConnected Function:
1. Check if there are enough edges to potentially connect all computers.
1. Initialize the union-find structure.
1. Iterate through the connections and use union-find to merge sets and track redundant edges.
1. Count the number of unique connected components.
1. Calculate the needed edges to connect all components.
1. Return the needed edges if the redundant edges are sufficient; otherwise, return -1.
