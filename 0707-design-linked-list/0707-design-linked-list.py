class MyLinkedList:

    def __init__(self):
        self.dq = deque([])

    def get(self, index: int) -> int:
        if index >= len(self.dq):
            return -1
        return self.dq[index]
        # print(self.dq)

    def addAtHead(self, val: int) -> None:
        self.dq.appendleft(val)
        # print(self.dq)

    def addAtTail(self, val: int) -> None:
        self.dq.append(val)
        # print(self.dq)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == len(self.dq):
            self.dq.append(val)
        elif index < len(self.dq):
            self.dq.insert(index, val)
        # print(self.dq)

    def deleteAtIndex(self, index: int) -> None:
        # print(self.dq)
        if index < len(self.dq):
            self.dq.rotate(-index)
            self.dq.popleft()
            self.dq.rotate(index)
        # print(self.dq)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)