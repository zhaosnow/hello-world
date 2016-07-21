tion for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        length //= 2
        if not head or not head.next:
            return True
        left, mid = head, head.next
        right = None if not mid else mid.next
        half_len = length
        while length:
            left = left.next
            mid = mid.next
            if right:
                right = right.next
            length -= 1
        while mid:
            mid.next = left
            left = mid
            mid = right
            if mid:
                right = mid.next
        tail = left
        while half_len:
            if tail.val != head.val:
                return False
            half_len -= 1
            tail = tail.next
            head = head.next
        return True
