from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
#         O(M * N) complexity
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.store:
#         O(M * N)
            # self.store[key] = {}
#         More efficient
            self.store[key] = SortedDict()
            
        self.store[key][timestamp] = value
        
    def get(self, key: str, timestamp: int) -> str:
#         O(M * N) complexity
        if key not in self.store:
            return ''
        
#         for curr_time in reversed(range(1, timestamp + 1)):
#             if curr_time in self.store[key]:
#                 return self.store[key][curr_time]
        
#         return ''

        it = self.store[key].bisect_right(timestamp)
        if it == 0:
            return ''
        
        return self.store[key].peekitem(it - 1)[1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)