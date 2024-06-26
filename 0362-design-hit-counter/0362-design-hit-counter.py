class HitCounter:

    def __init__(self):
        self.q = deque([])

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        if self.q:
            a = self.q[0]
            print(timestamp, self.q, a)
        while self.q and a < timestamp - 299:
            self.q.popleft()
            print(self.q)
            if self.q:
                a = self.q[0]
        return len(self.q)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)