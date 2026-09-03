# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = "~"
        
        def dfs(node, path):
            nonlocal ans
            if not node:
                return 

            path.append(chr(node.val + ord('a')))

            if not node.left and not node.right:
                str_path = "".join(reversed(path[:]))

                ans = min(ans, str_path)

            dfs(node.left, path)
            dfs(node.right, path)

            path.pop()

        dfs(root, [])
        return ans

        