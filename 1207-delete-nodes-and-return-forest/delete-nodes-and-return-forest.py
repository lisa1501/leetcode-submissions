# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        nodes_to_delete = set(to_delete)
        forest = []

        def dfs(node):
            if not node:
                return None

            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            if node.val not in nodes_to_delete:
                return node
            else:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None

        ans = dfs(root)

        if ans:
            forest.append(ans)
        return forest


        