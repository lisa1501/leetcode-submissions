# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans

            if not node:
                return []

            if not node.left and not node.right:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)

            res = []

            for l in left:
                if l + 1 <= distance:
                    res.append(l+1)

            for r in right:
                if r + 1 <= distance:
                    res.append(r+1)  

            for l in left:
                for r in right:
                    if (l+r) <= distance:
                        ans += 1  

            return res

        dfs(root)
        return ans
        