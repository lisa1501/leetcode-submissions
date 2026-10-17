# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.arr = []
        self.cur_idx = 0
        self.inOrder(root)
        print(self.arr)

    def inOrder(self, root):
        if not root:
            return

        self.inOrder(root.left)
        self.arr.append(root.val)
        self.inOrder(root.right)

    def next(self) -> int:
        val = self.arr[self.cur_idx]
        self.cur_idx += 1
        return val
        
    def hasNext(self) -> bool:
        return self.cur_idx <= len(self.arr) - 1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()