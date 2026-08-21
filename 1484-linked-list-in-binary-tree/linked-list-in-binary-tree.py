# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def match(a, b):
            if not b:
                return True
            if not a:
                return False

            if a.val != b.val:
                return False

            return match(a.left, b.next) or match(a.right, b.next)
        
        def dfs(node):
            if not node:
                return False

            if match(node, head):
                return True

            return dfs(node.left) or dfs(node.right)
        return dfs(root)
        