# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBSTHelper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            if not isBSTHelper(node.right, node.val, upper) or not isBSTHelper(node.left, lower, node.val):
                return False

            return True

        return isBSTHelper(root)