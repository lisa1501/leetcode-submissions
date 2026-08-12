# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([(root,1)])

        while q:
            cur_width = q[-1][1] - q[0][1] + 1
            ans = max(ans, cur_width)
            
            for i in range(len(q)):
                node, idx = q.popleft()
                if node:
                    if node.left:
                        q.append((node.left, idx*2))

                    if node.right:
                        q.append((node.right, idx*2+1))
        return ans