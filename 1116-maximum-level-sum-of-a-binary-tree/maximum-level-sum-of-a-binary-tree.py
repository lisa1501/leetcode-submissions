# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        max_level = None
        q = deque([(root, 1)])

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node, level = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append((node.left, level+1))
                if node.right:
                    q.append((node.right, level+1))

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

        return max_level

                


        