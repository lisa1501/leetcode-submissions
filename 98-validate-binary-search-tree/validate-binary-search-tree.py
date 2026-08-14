# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, mxa_val):
            if not node:
                return True

            if not (min_val < node.val < mxa_val):
                return False

            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, mxa_val)


        return dfs(root, float('-inf'), float('inf'))
        