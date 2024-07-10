O(n^3) but within time limit. Use grid to save distances since lots of edges. Only caveat is w​hen updating, the middle index `k` needs to be the outermost loop or will result in logical error.
1. Initialize Distance Matrix: Create an n x n distance matrix initialized to infinity (inf), with the diagonal set to zero (distance to itself is zero).
1. Fill Initial Distances: Use the edges array to fill in the initial distances between directly connected cities.
2. Floyd-Warshall Algorithm: Update the distance matrix to find the shortest paths between all pairs of cities.
3. Count Reachable Cities: For each city, count the number of cities that are reachable within the given distance threshold.
4. Determine Result: Find the city with the smallest number of reachable cities. If there are ties, choose the city with the greatest number.
