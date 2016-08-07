# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = list()
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        return self.build(nums, 0, len(nums) - 1)
        
    def build(self, nums, start, end):
        if start > end:
            return None
        elif start == end:
            root = TreeNode(nums[start])
            return root
        else:
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = self.build(nums, start, mid - 1)
            root.right = self.build(nums, mid + 1, end)
            return root
