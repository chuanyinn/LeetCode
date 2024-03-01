class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_score = -1
        result = float('inf')

        for divisor in divisors:
            current_score = sum(1 for num in nums if num % divisor == 0)
            
            if current_score > max_score or (current_score == max_score and divisor < result):
                max_score = current_score
                result = divisor

        return result