# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        a = []
        b = []
        def dfs(node, path):
            if not node:
                return 
            if not node.left and not node.right:
                path.append(node.val)
            left = dfs(node.left, path)
            right = dfs(node.right, path)
        dfs(root1, a)
        dfs(root2, b)
        return a == b