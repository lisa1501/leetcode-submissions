# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([(root, False)])

        while q:
            for _ in range(len(q)):
                node, isLeft = q.popleft()

                if isLeft and not node.left and not node.right:
                    ans += node.val

                if node.left:
                    q.append((node.left, True))

                if node.right:
                    q.append((node.right, False))

        return ans



        