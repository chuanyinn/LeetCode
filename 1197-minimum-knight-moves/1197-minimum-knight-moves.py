class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [(1, 2), (2, 1), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1)]
        
#         BFS queue, starting from (0, 0) with 0 steps
        queue = deque([(0, 0, 0)])
        visited = set((0, 0))
        
        while queue:
            cur_x, cur_y, steps = queue.popleft()
            
            if cur_x == x and cur_y == y:
                return steps
            
            for d in dirs:
                new_x, new_y = cur_x + d[0], cur_y + d[1]
                
                if (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, steps + 1))
            