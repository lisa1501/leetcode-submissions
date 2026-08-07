# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, count):
            nonlocal ans

            if not node:
                return 
                
            count[node.val] += 1

            if not node.left and not node.right:
                odd = 0
                for val in count.values():
                    if val % 2 == 1:
                        odd += 1

                if odd <= 1:
                    ans += 1

            dfs(node.left, count)
            dfs(node.right, count)

            count[node.val] -= 1

        dfs(root, count = defaultdict(int))
        return ans