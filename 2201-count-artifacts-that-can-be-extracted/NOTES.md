The important thing is that if a cell is excavated, ​all the cells within the artifact need to be excavated for it to be count. I initally pre-process a nxn matrix, then add counts. But that's incorrect.

Approach
1. Track the Covered Cells: Create a set to store the cells that have been dug.
2. Map each artifact to the set of its covered cells. Store in a list of sets. This helps in quickly checking which parts of the artifact are still buried.
3. For each artifact, check if all its cells are in the set of dug cells. Use `issubset` function.
