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
        # [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
        # bfs, [[1],[4,3],[7,6,8,5], [9,10]]
        # helper func, swap items, make nested list a sorted list, how many time swaping is => the minimum number of operations we needed 
        # [4,3] => sorted ,[3,4] store, num to idx [4,3] => {4:0, 3:1}, 
        # time : helper = o(nlogn) + O(n) = O(nlogn) bfs: O(n), total =O(nlogn)
        # space :O(n)

        ans = 0
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans += self.minSwap(level)      

        return ans

        

        

            



            

