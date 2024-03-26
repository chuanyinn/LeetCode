class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp: {position: count}
#         dp = defaultdict(int)
#         max_val = 0
#         for n1 in nums1:
#             new_dp = defaultdict(int)
#             inds = [index for index, value in enumerate(nums2) if value == n1]
#             # print(inds)
#             if not inds:
#                 dp = defaultdict(int)
#             else:
#                 for ind in inds:
#                     if (ind - 1) in dp:
#                         new_dp[ind] = dp[ind-1] + 1
#                     else:
#                         new_dp[ind] = 1
#                 dp = new_dp
#                 # print(dp)
#                 max_val = max(max_val, max(dp.values()))
        
#         return max_val
    
#         ChatGPT
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        max_length = 0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    max_length = max(max_length, dp[i][j])
                    
        return max_length