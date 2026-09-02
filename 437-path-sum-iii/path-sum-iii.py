# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        path_sums = defaultdict(int)
        path_sums[0] = 1
        def dfs(node, path_sum):
            nonlocal ans

            if not node:
                return 

            path_sum += node.val

            ans += path_sums[path_sum - targetSum]

            path_sums[path_sum] += 1

            dfs(node.left, path_sum)
            dfs(node.right, path_sum)

            path_sums[path_sum] -= 1

        dfs(root, 0)
        return ans
        