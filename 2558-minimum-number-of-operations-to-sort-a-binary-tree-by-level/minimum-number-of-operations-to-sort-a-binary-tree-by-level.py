# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minSwap(self, arr: list) -> int:
        swaps = 0
        sorted_arr = sorted(arr)
        num_to_idx = {}
        for i in range(len(arr)):
            num = arr[i]
            num_to_idx[num] = i

        for i in range(len(arr)):
            if arr[i] != sorted_arr[i]:
                idx = num_to_idx[sorted_arr[i]] 
                arr[i], arr[idx] = arr[idx], arr[i] 

                num_to_idx[arr[i]] = i 
                num_to_idx[arr[idx]] = idx 

                swaps += 1

        return swaps
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        ans = 0
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

        ans = 0
        for level in res:
            ans += self.minSwap(level)
        return ans

        

        

            



            

