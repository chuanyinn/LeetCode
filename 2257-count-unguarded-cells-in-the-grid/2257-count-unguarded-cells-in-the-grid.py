class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        GUARD, WALL, GUARDED = 'G', 'W', 1
        
        for row, col in guards:
            grid[row][col] = GUARD
        for row, col in walls:
            grid[row][col] = WALL
            
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for row, col in guards:
            for dr, dc in dirs:
                r, c = row + dr, col + dc
                while 0 <= r < m and 0 <= c < n:
                    if grid[r][c] in (GUARD, WALL):
                        break
                    if grid[r][c] == 0:
                        grid[r][c] = GUARDED
                    r += dr
                    c += dc
        print(grid)
        
        unguarded_count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    unguarded_count += 1
        
        return unguarded_count
            
            
#         guarded = set()
#         dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
#         for guard in guards:
#             gi, gj = guard
#             for dir_ in dirs:
#                 dri, drj = dir_[0], dir_[1]
#                 ni, nj = gi + dri, gj + drj
#                 while (0 <= ni < m) and (0 <= nj < n):
#                     if ([ni, nj] in walls) or ([ni, nj] in guards):
#                         break
#                     guarded.add((ni, nj))
#                     ni += dri
#                     nj += drj
#         print(guarded)
        
#         return m * n - len(guards) - len(walls) - len(guarded)
    
    