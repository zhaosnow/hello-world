# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.solve(root)
        
    def solve(self, root):
        if not root or (not root.left and not root.right):
            return root
        else:
            left = self.solve(root.left)
            right = self.solve(root.right)
            root.left = None
            root.right = left
            cur = root
            while cur.right:
                cur = cur.right
            cur.right = right
            return root
