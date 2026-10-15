# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(node):
            if not node:
                return None

            if node.val == startValue or node.val == destValue:
                return node

            left = lca(node.left)
            right = lca(node.right)

            if left and right:
                return node
            if left:
                return left
            return right

        ancesstor = lca(root)

        def dfs(node, target, path):
            if not node:
                return False

            if node.val == target:
                return True

            path.append("L")
            if dfs(node.left, target, path):
                return True
            path.pop()

            path.append("R")
            if dfs(node.right, target, path):
                return True
            path.pop()

            return False
        
        up = []
        down = []
        dfs(ancesstor, startValue, up)
        dfs(ancesstor, destValue, down)

        return "U"*len(up) + "".join(down)