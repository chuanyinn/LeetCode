class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        half_size = (len(arr) + 1) // 2
        
        sorted_count = sorted(counter.values(), reverse=True)
        
        acc = 0
        res = 0
        for v in sorted_count:
            acc += v
            res += 1
            if acc >= half_size:
                return res
        
        return res