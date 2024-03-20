class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        prefix_sum = 0
        total_subarrays = 0

        for num in nums:
            prefix_sum += num
            # if prefix_sum - k exists in prefix_sum_count, it means there is a subarray
            total_subarrays += prefix_sum_count[prefix_sum - k]
            prefix_sum_count[prefix_sum] += 1
        
        return total_subarrays