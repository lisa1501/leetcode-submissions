# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        heap = []
        q = deque([root])
        while q:
            level_sum = 0
            for _ in range(len(q)):

                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            heapq.heappush(heap, level_sum)

            if len(heap) > k:
                heapq.heappop(heap)

        if len(heap) < k:
            return -1

        return heap[0]


        