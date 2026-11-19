# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        is_balanced = True
        def dfs(node):
            nonlocal is_balanced
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diff = abs(left - right)
            if diff > 1:
                is_balanced = False
            return 1 + max(left, right)
        dfs(root)
        return is_balanced
        