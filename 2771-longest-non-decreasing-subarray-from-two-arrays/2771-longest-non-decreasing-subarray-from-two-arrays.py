class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
#         keep track of max non-decreasing subarray length if number ends with num1 or num2
        dp1 = [0] * n
        dp2 = [0] * n
        dp1[0], dp2[0] = 1, 1
        
        res = 1
        
        for i in range(1, n):
            dp1[i] = max(int(nums1[i] >= nums1[i-1]) * dp1[i-1], 
                         max(int(nums1[i] >= nums2[i-1]) * dp2[i-1], 0)) + 1
            dp2[i] = max(int(nums2[i] >= nums1[i-1]) * dp1[i-1], 
                         max(int(nums2[i] >= nums2[i-1]) * dp2[i-1], 0)) + 1
            res = max(res, max(dp1[i], dp2[i]))
        
        return res