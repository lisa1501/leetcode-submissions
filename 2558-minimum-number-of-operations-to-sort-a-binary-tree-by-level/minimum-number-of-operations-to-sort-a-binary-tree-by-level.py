# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minSwaps(self, arr: list) -> int:
        # Temporary array to store elements in sorted order
        temp = sorted(arr)
        
        # Hashing elements with their correct positions
        pos = {}
        for i in range(len(arr)):
            pos[arr[i]] = i
        
        swaps = 0
        for i in range(len(arr)):
            if temp[i] != arr[i]:
                
                ind = pos[temp[i]]
                arr[i], arr[ind] = arr[ind], arr[i]

                pos[arr[i]] = i
                pos[arr[ind]] = ind

                swaps += 1
        return swaps

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])

        ans = 0

        while q:

            level = []

            for _ in range(len(q)):
                
                node = q.popleft()
                if node:
                    level.append(node.val)

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

            ans += self.minSwaps(level)

            print(level)
        return ans
        