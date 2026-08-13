# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        q = deque([root])
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level_sum += node.val

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            heapq.heappush(sums, level_sum)
            if len(sums) > k:
                heapq.heappop(sums)
        if len(sums) < k:
            return -1
        return sums[0]
        