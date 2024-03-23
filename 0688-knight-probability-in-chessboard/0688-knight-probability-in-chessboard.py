class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = {(-1, -2), (-2, -1), (1, -2), (2, -1), (1, 2), (2, 1), (-1, 2), (-2, 1) }
        
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1

        for _ in range(k):
            new_dp = [[0] * n for _ in range(n)]

            # Iterate over each cell
            for r in range(n):
                for c in range(n):
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            new_dp[nr][nc] += dp[r][c] / 8
            
            dp = new_dp 
        
        total_ways = sum(sum(row) for row in dp)
        return total_ways