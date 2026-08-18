# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heigh = {}
        def get_heigh(node):
            if not node:
                return 0

            left = get_heigh(node.left)
            right = get_heigh(node.right)
            node_heigh = 1 + max(left, right)
            heigh[node.val] = node_heigh
            return node_heigh

        get_heigh(root)

        hm = {}
        def dfs(node, depth, restHeigh):
            if not node:
                return 0

            hm[node.val] = restHeigh

            rightHeigh = depth
            if node.right:
                rightHeigh = depth + heigh[node.right.val]

            dfs(node.left, depth+1, max(restHeigh, rightHeigh))

            leftHeigh = depth
            if node.left:
                leftHeigh = depth + heigh[node.left.val]

            dfs(node.right, depth+1, max(restHeigh, leftHeigh))

        dfs(root, 0, 0)
        
        res = []
        for q in queries:
            res.append(hm[q])
        return res


        

       


        