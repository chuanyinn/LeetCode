1. Depth-first search to handle the problem recursively. Define a helper function `dfs(r, c)`, and keep track of visited blocks.
2. Base case: if position is the destination (True) or if position is in visited (False). Iterative case: walking along the four main directions until hitting the wall, if one of them is True then return True. Otherwise return False. (This essentially propagates the path backward).
3. ​To ensure that the ball doesn't stop rolling, make sure to evaluate only outside the while loop, instead of each step inside the while loop.
