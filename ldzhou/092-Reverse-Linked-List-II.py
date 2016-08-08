# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 就是常规思路

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        fake_head = ListNode(0)
        fake_head.next = head
        pre = fake_head
        for i in range(m - 1):
            pre = pre.next
        left = pre.next
        mid = left.next
        right = None
        if mid:
            right = mid.next
        for i in range(n - m):
            mid.next = left
            left = mid
            mid = right
            if mid:
                right = mid.next
        post = mid
        pre.next.next = post
        pre.next = left
        return fake_head.next
