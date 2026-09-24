# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode | None) -> bool:
        q = deque([root])
        res = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        for i in range(len(res)):
            if i % 2 == 0:
                prev_val = float('-inf')
                for num in res[i]:
                    if num % 2 == 0:
                        return False

                    if num > prev_val:
                        prev_val = max(prev_val, num)
                    else:
                        return False    
            else:
                prev_val = float('inf')
                for num in res[i]:

                    if num % 2 == 1:
                        return False

                    if num < prev_val:
                        prev_val = min(prev_val, num)         
                    else:
                        return False
                        
        return True




                

        