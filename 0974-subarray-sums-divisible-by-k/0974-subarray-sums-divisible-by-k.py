class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod_count = defaultdict(int)
        mod_count[0] = 1
        
        current_sum = 0
        result = 0
        
        for num in nums:
            current_sum += num
            remainder = current_sum % k
            
            # if remainder < 0:
            #     remainder += k
            
            if remainder in mod_count:
                result += mod_count[remainder]
            
            mod_count[remainder] += 1
            
        return result