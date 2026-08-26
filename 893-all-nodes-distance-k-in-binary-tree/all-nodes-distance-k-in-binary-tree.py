# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent ={}
        def dfs(node, par):
            if not node:
                return 

            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        visited = set()
        visited.add(target)
        q = deque([(target, 0)])
        res = []
        
        while q:
            node, distance = q.popleft()

            if distance == k:
                res.append(node.val)

            for nei in (node.left, node.right, parent[node]):
                if nei and nei not in visited:
                    visited.add(nei)
                    q.append((nei, distance+1))
        return res