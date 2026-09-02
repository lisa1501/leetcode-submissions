# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0,0)

            robe_left_node, skip_left_node = dfs(node.left)
            robe_right_node, skip_right_node = dfs(node.right)

            robe_node = node.val + skip_left_node + skip_right_node

            skip_node = max(robe_left_node, skip_left_node) + max(robe_right_node, skip_right_node)

            return (robe_node, skip_node)
            
        return max(dfs(root))
        