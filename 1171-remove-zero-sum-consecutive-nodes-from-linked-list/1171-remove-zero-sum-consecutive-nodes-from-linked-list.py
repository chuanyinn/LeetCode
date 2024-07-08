# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Initialize a dummy node
        dummy = ListNode(0)
        dummy.next = head
        
        # Step 2: Use a hash map to store cumulative sums
        sum_map = {}
        current = dummy
        cumulative_sum = 0
        
        # Step 3: Traverse the list
        while current:
            cumulative_sum += current.val
            if cumulative_sum in sum_map:
                prev = sum_map[cumulative_sum].next
                temp_sum = cumulative_sum
                while prev != current:
                    temp_sum += prev.val
                    sum_map.pop(temp_sum)
                    prev = prev.next
                sum_map[cumulative_sum].next = current.next
            else:
                sum_map[cumulative_sum] = current
            current = current.next
        
        return dummy.next
        
#         sum_dict = {0: 0}
#         num_arr = []
#         cur_sum = 0
#         cur_ind = 0
#         node = head
        
#         while node:
#             cur_ind += 1
#             cur_sum += node.val
#             num_arr.append(node.val)
#             if cur_sum in sum_dict:
#                 prev_ind = sum_dict[cur_sum]
#                 items = {k: v for k, v in sum_dict.items()}
#                 for k, v in items.items():
#                     if prev_ind <= v < cur_ind:
#                         sum_dict.pop(k)
#             else:
#                 sum_dict[cur_sum] = cur_ind
#             node = node.next
        
#         return [num_arr[v-1] for k, v in sum_dict.items()]