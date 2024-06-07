class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        if k == 1:
            return all(x >= 0 for x in nums)
        
        diff = [0] * (n + 1)
        
        current_decrement = 0
        
        for i in range(n):
            current_decrement += diff[i]
            nums[i] -= current_decrement
            
            if nums[i] < 0:
                return False
            
            if nums[i] == 0:
                continue
            
            if i + k > n:
                return False
            
            current_decrement += nums[i]
            if i + k < n:
                diff[i + k] -= nums[i]
            
        return True
        
#         i = 0
#         while i < len(nums) - k + 1:
#             if nums[i] > 0:
#                 min_num = nums[i]
#                 for di in range(k):
#                     min_num = min(min_num, nums[i+di])
#                 print(min_num, i, nums[i])
#                 if min_num < nums[i]:
#                     return False
#                 for di in range(k):
#                     nums[i+di] -= min_num
#             i += 1
        
#         if any(nums) != 0:
#             return False
        
#         return True            