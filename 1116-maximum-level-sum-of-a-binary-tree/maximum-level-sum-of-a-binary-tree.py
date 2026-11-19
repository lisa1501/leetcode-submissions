# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        levels = []
        def dfs(node, level):
            if not node:
                return 

            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)

            left = dfs(node.left, level+1)
            right = dfs(node.right, level+1)
        dfs(root, 0)

        max_sum = float('-inf')
        max_level = None

        for i, level in enumerate(levels):
            if sum(level) > max_sum:
                max_sum = sum(level)
                max_level = i + 1

        return max_level
