# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.solve(root, 0)
        
    def solve(self, root, num): # 以root为跟的tree, 路径下来的结果是num, 求结果.
        if not root:
            return 0
        elif not root.left and not root.right:
            return num * 10 + root.val
        else:
            return self.solve(root.left, num * 10 + root.val) + self.solve(root.right, num * 10 + root.val)
