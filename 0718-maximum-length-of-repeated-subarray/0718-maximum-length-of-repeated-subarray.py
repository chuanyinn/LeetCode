class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp: {position: count}
        dp = defaultdict(int)
        max_val = 0
        for n1 in nums1:
            new_dp = defaultdict(int)
            inds = [index for index, value in enumerate(nums2) if value == n1]
            # print(inds)
            if not inds:
                dp = defaultdict(int)
            else:
                for ind in inds:
                    if (ind - 1) in dp:
                        new_dp[ind] = dp[ind-1] + 1
                    else:
                        new_dp[ind] = 1
                dp = new_dp
                # print(dp)
                max_val = max(max_val, max(dp.values()))
        
        return max_val