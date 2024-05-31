class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (high + 1)
        dp[0] = 1
        
        for length in range(1, high+1):
            if length >= zero:
                dp[length] = (dp[length] + dp[length - zero]) % MOD
            if length >= one:
                dp[length] = (dp[length] + dp[length - one]) % MOD
        
        res = 0
        for length in range(low, high+1):
            res = (res + dp[length]) % MOD
            
        return res
        
#         strings = deque([''])
#         res = 0
        
#         while strings:
#             s = strings.pop()
#             if low <= len(s) <= high:
#                 res += 1
#             if len(s) + zero <= high:
#                 strings.append(s + '0'*zero)
#             if len(s) + one <= high:
#                 strings.append(s + '1'*one)
#             print(strings)
        
#         return res