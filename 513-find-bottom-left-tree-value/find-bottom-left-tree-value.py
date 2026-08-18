# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = 0
        max_depth = -1

        def dfs(node, depth):
            nonlocal ans, max_depth
            if not node:
                return 0

            if depth > max_depth:
                max_depth = depth
                ans = node.val

            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)

        dfs(root, 0)
        return ans

        