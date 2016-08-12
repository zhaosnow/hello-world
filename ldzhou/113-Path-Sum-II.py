# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.ans = []
        self.solve(root, [], 0, sum)
        return self.ans
        
    def solve(self, root, path, path_sum, target):
        path_sum += root.val
        path.append(root.val)
        if not root.left and not root.right:
            if path_sum == target:
                self.ans.append(path)
        else:
            if root.left:
                self.solve(root.left, list(path), path_sum, target)
            if root.right:
                self.solve(root.right, list(path), path_sum, target)

