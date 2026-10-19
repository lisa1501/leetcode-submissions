# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""
        def dfs(node):
            nonlocal res
            if not node:
                return res

            res += str(node.val)

            if node.left:
                res += "(" + self.tree2str(node.left) + ")"

            if node.right:
                if not node.left:
                    res += "()"

                res += "(" + self.tree2str(node.right) + ")"
        dfs(root)
        return res