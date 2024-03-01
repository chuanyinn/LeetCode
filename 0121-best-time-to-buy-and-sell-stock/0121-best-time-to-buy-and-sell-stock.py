class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         one pass approach
#         keep track of the best buy day so far
#         keep track of the largest difference so far

        max_diff = 0
        min_so_far = 10000
        
        for i in range(len(prices)):
            if prices[i] < min_so_far:
                min_so_far = prices[i]
            else:
                max_diff = max(max_diff, prices[i] - min_so_far)
        
        return max_diff