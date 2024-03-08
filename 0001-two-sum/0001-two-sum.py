class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of numbers
        num_indices = {}

        # Iterate through the array 
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_indices:
                return [num_indices[complement], i]
            
            # If not found, add the current number and index to dictionary
            num_indices[num] = i

        # If no solution is found
        return []