# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # dfs, walk through on the tree, dfs return bool, if cur node val == target val, T else F, if not node F
        # two lists, one list store the path from node to start value, one store the path from node to dest value, for left node list append "L", right node list append "R"
        # LCA: Find common prefix, root = [5,1,2,3,null,6,4], startValue = 6, destValue = 4, 
        # list1=[R,L] list2=[R,R]  node 2 is LCA of startValue = 6, destValue = 4, 
        # get the idx Find common prefix,  how many "L" from LCA idx means how many Up
        # return up + and join list2
        # Time:  O(n) Space: O(h)
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
        dfs(root, startValue, start_path)
        dfs(root, destValue, dest_path)
        
        # Find common prefix
        i = 0 
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1

        # start -> LCA
        up = "U" * (len(start_path) - i)

        # LCA -> destination
        down = "".join(dest_path[i:])

        return up + down




        

        