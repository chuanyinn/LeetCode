class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dp = defaultdict(int)
        res = 0
        
        for t in time:
            remainder = t % 60
            complement = (60 - t) % 60
            res += dp[complement]
            dp[remainder] += 1
        
        return res