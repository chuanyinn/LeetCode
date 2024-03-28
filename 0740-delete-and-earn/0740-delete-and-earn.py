class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_num = max(nums)
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += num
        
        # Apply dynamic programming
        dp = [0] * (max_num + 1)
        dp[1] = freq[1]

        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + freq[i])

        return dp[max_num]
