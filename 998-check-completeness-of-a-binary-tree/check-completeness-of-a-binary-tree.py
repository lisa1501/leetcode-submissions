# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        seen_null = False

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    if seen_null == True:
                        return False

                    q.append(node.left)
                    q.append(node.right)
                    
                else:
                    seen_null = True
                
        return True

        