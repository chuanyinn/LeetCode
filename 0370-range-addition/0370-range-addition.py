class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # Initialize an array with zeros
        arr = [0] * length

        # Apply each update operation
        for start, end, inc in updates:
            # Increment the value at the starting index
            arr[start] += inc
            # Decrement the value at the index after the ending index
            if end + 1 < length:
                arr[end+1] -= inc
            
        # Perform prefix sum to get the final result
        for i in range(1, length):
            arr[i] += arr[i-1]

        return arr
