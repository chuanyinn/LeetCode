class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ordered_dict = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.ordered_dict:
            value = self.ordered_dict.pop(key)
            self.ordered_dict[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.ordered_dict) < self.capacity or key in self.ordered_dict:
            if key in self.ordered_dict:
                self.ordered_dict.pop(key)
            self.ordered_dict[key] = value
        else:
            # Evict the least recently used key and add the new key-value pair
            self.ordered_dict.popitem(last=False)
            self.ordered_dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)