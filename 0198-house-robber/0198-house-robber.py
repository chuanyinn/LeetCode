class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
#         Initialize an array to store the max amount of money stored at each house
        dp = [0] * len(nums)
#         Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
#         Iterate through the rest of the houses, updating the max amount stored at each house
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        return dp[-1]

        
#         takes = [nums[0]]
#         skips = [0]
#         for num in nums[1:]:
#             if len(skips) > 2:
#                 temp_skip = max(skips[-1], skips[-2])
#             else:
#                 temp_skip = skips[-1]
#             skips.append(takes[-1])
#             takes.append(num + temp_skip)
#             print(takes, skips)
        
#         return max(takes[-1], skips[-1])