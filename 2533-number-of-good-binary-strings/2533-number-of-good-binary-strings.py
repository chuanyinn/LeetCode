class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        dp = [0] * (maxLength + 1)
        dp[0] = 1
        MOD = 10**9 + 7
        res = 0
        
        for i in range(min(oneGroup, zeroGroup), maxLength + 1):
            if i >= oneGroup:
                dp[i] = (dp[i] + dp[i - oneGroup]) % MOD
            if i >= zeroGroup:
                dp[i] = (dp[i] + dp[i - zeroGroup]) % MOD
                
        res = sum(dp[minLength:])
        
        return res % MOD