# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.d = dict()
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.solve(root)
        
    def solve(self, root):
        if not root:
            return 0
        elif not root.left and not root.right:
            return root.val
        else:
            if root in self.d:
                return self.d[root]
            ans = 0
            ans = max(self.solve(root.left) + self.solve(root.right), ans)
            left = right = 0
            if root.left:
                left = max(left, self.solve(root.left.left) + self.solve(root.left.right))
            if root.right:
                right = max(right, self.solve(root.right.left) + self.solve(root.right.right))
            ans = max(ans, root.val + left + right)
            self.d[root] = ans
            return ans
