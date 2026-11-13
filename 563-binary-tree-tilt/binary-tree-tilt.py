# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

    #       1
    #    2    3
    #  N  N  N N 
    #  0  0  0  0

    #  substree of node 2 - >  2 N N = 2.val + 0 +0  = 2
    #  substree of node 3 - >  3 N N = 3.val + 0 +0  = 3

    #  1
    # 2 3 =>  abs(2-3) = 1

    # dfs traverse, 
    # if not node, None node -> 0
    # leaf node: -> node.val + left child + right child
    # tilt
    # tilt increametn by cur sub sub tree value => abs(dfs(left child) - dfs(right child))

    # time :O(n) space: heigh of this binary tree

        tilt = 0
        def dfs(node):
            nonlocal tilt
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            tilt += abs(left - right)
            return node.val + left + right
        dfs(root)
        return tilt
