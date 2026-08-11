# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # time:O(n), space:O(n)
        res = []
        if not root:
            return res
        q = deque([root])

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(level)

        for i in range(len(res)):
            if i % 2 == 0:
                prev = float('-inf')
                for ele in res[i]:
                    if ele % 2 == 0:
                        return False
                    if ele <= prev:
                        return False
                    prev = ele
            else:
                prev = float('inf')
                for ele in res[i]:
                    if ele % 2 == 1:
                        return False
                    if ele >= prev:
                        return False
                    prev = ele
        return True
                    
            




        