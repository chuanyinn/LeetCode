class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # find thieves
        thieves = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        print(thieves)
        
        # Step 1: calculate safety factor of each cell with multi-source breadth-first Search (BFS)
        multi_source_queue = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    multi_source_queue.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1
            
        while multi_source_queue:
            size = len(multi_source_queue)
            while size > 0:
                r, c = multi_source_queue.popleft()
                val = grid[r][c]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == -1:
                        grid[nr][nc] = val + 1
                        multi_source_queue.append((nr, nc))
                size -= 1
        
        # brute force approach would be O(n^4)
        # safe_grid = [[0] * C for _ in range(R)]
        # for r in range(R):
        #     for c in range(C):
        #         safe = float('inf')
        #         for ti, tj in thieves:
        #             safe = min(safe, abs(r - ti) + abs(c - tj))
        #         safe_grid[r][c] = safe
        
        
        # Step 2: calculate safety path by revised greedy Dijkstra's algorithm 
        pq = [[-grid[0][0], 0, 0]] # [maximum_safeness_till_now, x-coordinate, y-coordinate]
        grid[0][0] = -1 # -1 means visited
        
        while pq:
            safeness, r, c = heapq.heappop(pq)
            
            if r == n - 1 and c == n - 1:
                return -safeness
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != -1:
                    heapq.heappush(pq, [-min(-safeness, grid[nr][nc]), nr, nc])
                    grid[nr][nc] = -1
            
        return -1