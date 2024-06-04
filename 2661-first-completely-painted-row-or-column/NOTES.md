Serparate initialization and iterative processing for quick access.

Initialization:
1. Create counters for each row and column to track how many cells have been painted.
1.Use a dictionary to map the values in mat to their respective positions for quick access.

Processing:
1.Iterate through each value in arr.
1.For each value, find its position in mat using the dictionary.
1.Increment the counters for the corresponding row and column.
1.Check if any row or column has been completely painted after each increment.​
