Multi-source breadth-first Search (BFS).
1. In a timestep need to do multiple things, thus requiring a for loop on the queue size inside the while loop.
2. Usage of deque instead of queue is important, as we need to `popleft()` so things follow logic.
3. Off-by-one error to be avoided in the end, when queue still points to the last orange, but they have already rotten.
