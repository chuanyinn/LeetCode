class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        R, C = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        fresh_oranges = 0
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        if fresh_oranges == 0:
            return 0
        
        t = 0
        while queue and fresh_oranges > 0:
            t += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        queue.append((nr, nc))
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return -1
                
        return t