class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            max_global = float('-inf')
            max_current = 0
            for num in arr:
                max_current = max(max_current + num, num)
                max_global = max(max_global, max_current)
            return max_global
        
        # 1. maximum sum subarray without circular wrapping
        max_sum_standard = kadane(nums)

        # 2. maximum sum subarray with circular wrapping
        total_sum = sum(nums)
        inverted_nums = [-num for num in nums]
        min_sum_circular = kadane(inverted_nums) + total_sum

        # if all results negative, return the result from case 1 
        if min_sum_circular == 0:
            return max_sum_standard
        return max(max_sum_standard, min_sum_circular)
