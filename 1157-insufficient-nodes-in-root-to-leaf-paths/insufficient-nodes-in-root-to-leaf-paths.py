# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node, curSum):
            if not node:
                return None
            curSum += node.val
            
            # Leaf
            if not node.left and not node.right:
                if curSum >= limit:
                    return node
                else:
                    return None

            node.left = dfs(node.left, curSum)
            node.right = dfs(node.right, curSum)

            # Both subtrees were insufficient
            if not node.left and not node.right: 
                return None

            return node

        return dfs(root, 0)
        