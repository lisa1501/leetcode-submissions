# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(node):
            if not node:
                return (0, 0)

            left_skip_node, left_take_node = dfs(node.left)
            right_skip_node, right_take_node = dfs(node.right)

            skip_node = max(left_skip_node, left_take_node) + max(right_skip_node, right_take_node)
            take_node = node.val + left_skip_node + right_skip_node

            return (skip_node, take_node)

        return max(dfs(root))
        