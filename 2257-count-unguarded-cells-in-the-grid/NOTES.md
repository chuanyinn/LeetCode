Initially TLE because doing too much in the nested for loop. Save time by pre-processing the grid to mark up the guard and wall locations, instead of doing the searching while in the for loop.
1. Initialize the grid: Create an m x n grid initialized to 0.
1. Mark guards and walls: Update the grid to mark positions of guards and walls.
1. Simulate guard vision: For each guard, mark all cells they can see in the four cardinal directions unless blocked by a wall or another guard.
1. Count unoccupied and unguarded cells: Traverse the grid and count cells that are neither occupied by a guard or a wall nor guarded.​
