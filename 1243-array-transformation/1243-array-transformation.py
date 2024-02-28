class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            new_arr = arr.copy()
            for i in range(1, len(arr)-1):
                if (arr[i-1] < arr[i]) and (arr[i+1] < arr[i]):
                    new_arr[i] -= 1
                elif (arr[i-1] > arr[i]) and (arr[i+1] > arr[i]):
                    new_arr[i] += 1
            if new_arr == arr:
                return arr
            arr = new_arr
            