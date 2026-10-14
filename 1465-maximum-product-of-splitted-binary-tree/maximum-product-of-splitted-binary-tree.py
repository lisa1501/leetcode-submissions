# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def getTotalSum(node):

            if not node:
                return 0

            left = getTotalSum(node.left)
            right = getTotalSum(node.right)

            return left + right + node.val

        total = getTotalSum(root)
        ans = 0

        def dfs(node):
            nonlocal ans, total
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            subtree_sum = node.val + left + right

            ans = max(ans, (total - subtree_sum) * subtree_sum)

            return subtree_sum

        dfs(root)
        return ans % (10**9+7)
        