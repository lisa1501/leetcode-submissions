# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #  dfs, 
        # path sum  =0
        # start with root, i
        # increase path sum by current node.val
        # parent node return path sum + parent ndoe val then transfer this to left and rieght child
        # when we met path sum == targetsum => ture
        # visiting all node, paths there is no path sum == target, return false
        # time :O(n),O(n)
        def dfs(node, path_sum):
            if not node:
                return False

            path_sum += node.val

            if not node.left and not node.right:
                return path_sum == targetSum

            left = dfs(node.left, path_sum) 
            right = dfs(node.right, path_sum)
        
            return left or right

        return dfs(root, 0)
        