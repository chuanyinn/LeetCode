# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            total_good = 0
            if node.val >= max_val:
                total_good += 1
                max_val = node.val
            total_good += dfs(node.left, max_val)
            total_good += dfs(node.right, max_val)
            return total_good

        return dfs(root, float('-inf'))