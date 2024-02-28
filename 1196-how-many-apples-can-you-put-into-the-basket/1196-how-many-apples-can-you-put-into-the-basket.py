class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        res = 0
        cur_sum = 0
        sorted_weights = sorted(weight)
        for i, w in enumerate(sorted_weights):
            cur_sum += w
            if cur_sum > 5000:
                return i
        return i+1