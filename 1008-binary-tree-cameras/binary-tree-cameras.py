# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        ans = 0

        has_camera = 1
        need_camera = 2
        cover_camera = 3

        def dfs(node):
            nonlocal ans
            if not node:
                return cover_camera

            left = dfs(node.left)
            right = dfs(node.right)

            if left == need_camera or right == need_camera:
                ans += 1
                return has_camera

            if left == has_camera or right == has_camera:
                return cover_camera

            

            return need_camera

            
        if dfs(root) == need_camera:
            ans += 1

        return ans
        