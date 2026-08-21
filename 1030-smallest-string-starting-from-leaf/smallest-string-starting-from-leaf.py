# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = "~"
        path = []
        def dfs(node):
            nonlocal ans
            if not node:
                return 
            path.append(chr(node.val + ord('a')))

            if not node.left and not node.right:
                str_path = "".join(reversed(path[:]))

                ans = min(ans, str_path)

            dfs(node.left)
            dfs(node.right)

            path.pop()

        dfs(root)
        return ans

        