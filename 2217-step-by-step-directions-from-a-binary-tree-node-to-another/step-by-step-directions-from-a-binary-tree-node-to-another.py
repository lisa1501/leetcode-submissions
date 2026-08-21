# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # from start, dest we can find lowest common ancessto LCA
        # start from the lca, dfss traverse, left and riight
        # path, is a lis, go to cur node left, if cur node is target val dfs => true
        # 5 -> 1 path append "L" , 1->3 path append "L" =>["L","L"]
        # 3 is target val, return T
        # if 6 is right child of 1, 
        # pop from path, ["L","L"] => ["L"] => we are node 1, 
        # then go to right, path appen "R" ["L","R"]
        # updtat "L" to U
        # joinn path and return 
        # time: O(n), space:O(h) n is num of node, blance h is heigh of the tree, worste O(n)
        def lca(node):
            if not node:
                return None

            if node.val == startValue or node.val == destValue:
                return node

            left = lca(node.left)
            right = lca(node.right)

            if left and right: # left=3, right=6 => return 5
                return node

            if left :
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

        start_path = []
        dest_path = []

        up = dfs(ancesstor, startValue, start_path)
        down = dfs(ancesstor, destValue, dest_path)

        return "U" * (len(start_path)) + "".join(dest_path)



        