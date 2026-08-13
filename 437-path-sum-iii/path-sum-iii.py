# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # dfs
        # mp, store path sum as key, and value freq
        # ans 0
        # parent node path sum plus node.val , then pass this info to left and right chile
        # keep adding child node val to path sum
        # if path_sum - target in mp, increase ans by path_sum - target
        # {10:1, 15:1, 18:1}
        # 10-8=2 =>0, 15-8=7=>0 , 18-8=10, ans+1
        # when left is done, for back to parent, mp[path sum] -=1 {}
        # return ans
        # time:O(n), space O(n)

        ans = 0
        count = defaultdict(int)
        count[0] = 1
        def dfs(node, path_sum):
            nonlocal ans
            if not node:
                return 

            path_sum += node.val

            ans += count[path_sum- targetSum]
            count[path_sum] += 1

            dfs(node.left, path_sum)
            dfs(node.right, path_sum)
 
            count[path_sum] -= 1

        dfs(root, 0)
        return ans         
        