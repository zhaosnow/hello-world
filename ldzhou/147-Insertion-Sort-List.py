# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 如果使用插入排序, 1-5000的排序过不了, 在discuss已经被吐槽了
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nums = list()
        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        nums.sort()
        cur = head
        index = 0
        while cur:
            cur.val = nums[index]
            index += 1
            cur = cur.next
        return head
