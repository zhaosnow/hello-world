# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        fake_odd = ListNode(0)
        fake_even = ListNode(0)
        cur_odd = fake_odd
        cur_even = fake_even
        flag = 1
        while cur:
            if flag:
                cur_odd.next = cur
                cur_odd = cur
                cur = cur.next
            else:
                cur_even.next = cur
                cur_even = cur
                cur = cur.next
            flag = 1 - flag
        cur_odd.next = fake_even.next
        cur_even.next = None
        return fake_odd.next
