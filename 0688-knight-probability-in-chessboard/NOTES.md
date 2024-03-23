1. dp to keep track of the number of ways the knight can reach each cell in exactly k moves
2. ​For each round, `dp` stores the intial probability, `new_dp` calculates new positions and store their probabilities, as 1/8 times previous. Eventually sum them all up because those are the only live setups
3. Initially I was thinking of deque or recursion, but that turned out to be over-complicated as it is not too hard to count how many ways there is
