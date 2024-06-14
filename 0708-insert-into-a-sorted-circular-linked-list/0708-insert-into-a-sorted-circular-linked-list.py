"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        
        if not head:
            new_node.next = new_node
            return new_node
        
        prev, current = head, head.next
        
        while True:
#             Case 1: Insert in the middle of the list
            if prev.val <= insertVal <= current.val:
                break
#             Case 2: Insert at the end f the list or at the start
            if prev.val > current.val:
                if insertVal >= prev.val or insertVal <= current.val:
                    break
            prev, current = current, current.next 
#             Case 3: Traversed all nodes and came back to the start node
            if prev == head:
                break
        
        prev.next = new_node
        new_node.next = current
        
        return head