# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(a, b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            if a.val != b.val:
                return False

            flip = dfs(a.left, b.right) and dfs(a.right, b.left)
            no_flip = dfs(a.left, b.left) and dfs(a.right, b.right)
            return flip or no_flip
            
        return dfs(root1, root2)
        