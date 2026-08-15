# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        def dfs(node, par):
            if not node:
                return 
            parents[node] = par
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)

        visit = set()
        visit.add(target)
        res = []
        q = deque([(target, 0)]) # node, distance from node to target
        while q:
            node, distance = q.popleft()
            if distance == k:
                res.append(node.val)

            for nei in (node.left, node.right, parents[node]):
                if nei and nei not in visit:
                    visit.add(nei)
                    q.append((nei, distance+1))
                        
        return res


