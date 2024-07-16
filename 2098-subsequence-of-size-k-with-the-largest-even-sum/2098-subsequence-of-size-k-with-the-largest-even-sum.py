class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        
        top_k_elements = nums[:k]
        current_sum = sum(top_k_elements)
        
        if current_sum % 2 == 0:
            return current_sum
        
        smallest_odd_in_k = float('inf')
        largest_even_outside_k = float('-inf')
        smallest_even_in_k = float('inf')
        largest_odd_outside_k = float('-inf')
        
        for num in top_k_elements:
            if num % 2 != 0 and num < smallest_odd_in_k:
                smallest_odd_in_k = num
            if num % 2 == 0 and num < smallest_even_in_k:
                smallest_even_in_k = num
        
        for num in nums[k:]:
            if num % 2 == 0 and num > largest_even_outside_k:
                largest_even_outside_k = num
            if num % 2 != 0 and num > largest_odd_outside_k:
                largest_odd_outside_k = num
        
        candidates = []
        
        if smallest_odd_in_k != float('inf') and largest_even_outside_k != float('-inf'):
            candidates.append(current_sum - smallest_odd_in_k + largest_even_outside_k)
        
        if smallest_even_in_k != float('inf') and largest_odd_outside_k != float('-inf'):
            candidates.append(current_sum - smallest_even_in_k + largest_odd_outside_k)
        
        if candidates:
            return max(candidates)
        else:
            return -1
        
#         if len(nums) == k:
#             if sum(nums) % 2 == 0:
#                 return sum(nums)
#             else:
#                 return -1
        
#         cur_list = nums[:k+1]
#         max_even_sum, max_odd_sum = 0, 0
#         if sum(cur_list) % 2 == 0:
#             max_even_sum = sum(cur_list)
#         else:
#             max_odd_sum = sum(cur_list)
#         evens = [x for x in cur_list if x % 2 == 0]
#         odds = [x for x in cur_list if x % 2 == 1]
#         heapq.heapify(evens)
#         heapq.heapify(odds)
        
        
#         for i in range(k, len(nums)):
#             num = nums[i]
#             if num % 2 == 0:
#                 min_even_num = heapq.heappop(evens)
#                 small = min(num, min_even_num)
#                 large = max(num, min_even_num)
#                 max_even_sum += (large - small)
#                 heapq.heappush(evens, large)
#             else:
#                 min_odd_num = heapq.heappop(odds)
#                 small = min(num, min_odd_num)
#                 large = max(num, min_odd_num)
#                 min_odd_num += (large - small)
#                 heapq.heappush(odds, large)
                
#         return max_even_sum