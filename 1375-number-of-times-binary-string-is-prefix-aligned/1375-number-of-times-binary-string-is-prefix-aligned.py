class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_flip = 0
        count = 0
        
        for i, flip in enumerate(flips):
            max_flip = max(max_flip, flip)
            if max_flip == i + 1:
                count += 1
                
        return count
        
#         n = len(flips)
#         s_arr = [0] * n
        
#         res = 0
#         for i, flip in enumerate(flips):
#             s_arr[flip - 1] = 1
#             if sum(s_arr[:i+1]) == i + 1:
#                 res += 1
        
#         return res