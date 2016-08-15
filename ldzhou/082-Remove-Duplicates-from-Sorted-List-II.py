# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        fake_head = ListNode(0)
        fake_head.next = head
        left, mid, right = fake_head, head, head.next
        while right:
            while right and mid.val == right.val:
                right = right.next
            if mid.next == right:
                left = mid
                mid = right
                if right:
                    right = right.next
            else:
                left.next = right
                mid = right
                if right:
                    right = right.next
        if mid and mid.next != right:
            left.next = right
        return fake_head.next
