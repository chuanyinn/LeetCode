class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_bits = max(candidates).bit_length()
        bit_count = [0] * max_bits
        
        for number in candidates:
            for i in range(max_bits):
                if number & (1 << i):
                    bit_count[i] += 1
                    
        return max(bit_count)
#         bins = [bin(candidate)[2:][::-1] for candidate in candidates]
#         n = len(candidates)
        
#         min_length = len(bins[0])
#         for c in bins:
#             min_length = min(min_length, len(c))
        
#         res = float('inf')
#         for i in range(min_length):
#             res = min(res, sum([int(b[1]) for b in bins]))

#         print(bins)
#         return res
        
