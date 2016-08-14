# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 常规解法
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        nums = list(range(1, n + 1))
        return self.solve(nums)
        
    def solve(self, nums):
        if not nums:
            return [None]
        elif len(nums) == 1:
            root = TreeNode(nums[0])
            return [root]
        else:
            ans = list()
            for i in range(len(nums)):
                lefts = self.solve(nums[:i])
                rights = self.solve(nums[i + 1:])
                for left in lefts:
                    for right in rights:
                        root = TreeNode(nums[i])
                        root.left = left
                        root.right = right
                        ans.append(root)
            return ans
