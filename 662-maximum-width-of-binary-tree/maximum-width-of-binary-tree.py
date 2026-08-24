# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])

        ans = 0

        while q:
            width = q[-1][1] - q[0][1] + 1
            ans = max(ans, width)

            for _ in range(len(q)):
                node, width = q.popleft()

                if node:
                    if node.left:
                        q.append((node.left, 2*width))
                    if node.right:
                        q.append((node.right, 2*width + 1))

        return ans


        