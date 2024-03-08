# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def subtree_sum(node):
            if not node:
                return 0
            return node.val + subtree_sum(node.left) + subtree_sum(node.right)

        total_sum = subtree_sum(root)

        def find_max_product(node):
            nonlocal total_sum
            if not node:
                return 0
            
            # Calculate the sum of the current subtree
            current_subtree_sum = node.val + find_max_product(node.left) + find_max_product(node.right)

            # Calculate the product of the current subtree and the remaining sum
            product = current_subtree_sum * (total_sum - current_subtree_sum)

            # Update the maximum product
            nonlocal max_product
            max_product = max(max_product, product)

            return current_subtree_sum
        
        max_product = 0
        find_max_product(root)

        return max_product % (10**9 + 7)