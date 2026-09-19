# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def isSameTrees(a, b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            if a.val != b.val:
                return False

            flip = isSameTrees(a.left, b.right) and isSameTrees(a.right, b.left)
            no_flip = isSameTrees(a.left, b.left) and isSameTrees(a.right, b.right)
            return flip or no_flip
            
        return isSameTrees(root1, root2)
        