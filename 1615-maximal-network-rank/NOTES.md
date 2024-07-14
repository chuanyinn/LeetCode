I used a defaultdict(list) to store connections, but handling `max_rank` when ties might happen is annoying. Instead, use a dictionary of int that stores just the rank, and a set of tuples to store all connections.
1. Count the Roads for Each City: Maintain a count of how many roads each city is connected to.
1. Count Shared Roads: Keep track of the roads shared between each pair of cities.
1. Calculate the Network Rank for Each Pair: For each pair of cities, calculate their network rank by summing their individual road counts and subtracting the shared road if they have one.
1. Find the Maximum Rank: Track the maximum network rank encountered during the calculations.​
