# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = []
        def dfs(node, depth):
            if not node:
                return 

            if len(levels) == depth:
                levels.append([])

            levels[depth].append(node.val)

            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)

        dfs(root, 0)

        max_leval = None
        max_val = float('-inf')

        for i in range(len(levels)):
            if sum(levels[i]) > max_val:
                max_val = sum(levels[i])
                max_level = i

        return max_level + 1