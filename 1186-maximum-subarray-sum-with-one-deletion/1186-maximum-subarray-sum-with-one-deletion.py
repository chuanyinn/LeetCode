class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        max_inclusive = float('-inf')
        max_exclusive = float('-inf')
        max_global = float('-inf')
        for num in arr:
            # Case exclusive, either add to already skipped, or skip this one
            max_exclusive = max(max_exclusive + num, max_inclusive)
            # Case inclusive, either continue with previous or start over
            max_inclusive = max(max_inclusive + num, num)
            max_global = max(max_exclusive, max_inclusive, max_global)
        return max_global