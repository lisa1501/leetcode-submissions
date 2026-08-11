# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # time:O(n), space:O(n)
        if not root: 
            return []
        
        q = deque([root])
        depth = 0
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if depth % 2 == 1: #odd level
                i = 0  # two pointers
                j = len(level)-1
                while i < j:
                    level[i].val, level[j].val = level[j].val, level[i].val #swap
                    i+=1 # move two pointers
                    j-=1
            depth += 1
        
        return root
        