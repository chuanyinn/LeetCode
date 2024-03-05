To solve this problem, you can use Depth-First Search (DFS) to traverse the connected cities and identify the provinces. Here's a Python function that implements this:

This function, findCircleNum, takes the isConnected matrix as input and returns the total number of provinces. It uses DFS to explore each city and mark all the connected cities within the same province. The provinces variable keeps track of the total number of provinces.
