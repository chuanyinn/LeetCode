class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        res = 0
        
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                if matrix[r - 1][c - 1] == '1':
                    dp[r][c] = min(dp[r - 1][c - 1],
                                   min(dp[r][c - 1], dp[r - 1][c])) + 1
                    res = max(res, dp[r][c])
                    
        return res ** 2