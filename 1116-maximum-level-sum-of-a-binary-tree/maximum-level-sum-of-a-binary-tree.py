# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = []

        def dfs(node, depth):
            if not node:
                return 

            if depth == len(res):
                res.append([])
            res[depth].append(node.val)

            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

        dfs(root, 0)

        max_val = float('-inf')
        max_val_level = None

        for i in range(len(res)):
            if sum(res[i]) > max_val:
                max_val = sum(res[i]) 
                max_val_level = i 

        return max_val_level + 1

        