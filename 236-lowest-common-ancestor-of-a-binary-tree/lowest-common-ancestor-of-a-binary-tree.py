# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(node):
            if not node:
                return None
            # p,q are node, is not val
            if node == p or node == q:
                return node

            left = lca(node.left)
            right = lca(node.right)

            if left and right:
                return node

            if left:
                return left

            return right

        return lca(root)
        