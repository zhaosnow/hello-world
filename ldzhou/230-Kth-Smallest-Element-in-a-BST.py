# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.path = list()
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.find_path(root)
        for i in range(k):
            node = self.path.pop()
            ans = node.val
            self.find_path(node.right)
        return ans
        
    def find_path(self, root):
        cur = root
        while cur:
            self.path.append(cur)
            cur = cur.left
