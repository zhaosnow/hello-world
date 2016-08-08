# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        if not length:
            return None
        k %= length
        fake_head1 = ListNode(0)
        fake_head2 = ListNode(0)
        fake_head1.next = head
        fake_head2.next = head
        cur = fake_head1
        
        for i in range(length - k):
            cur = cur.next
            fake_head2.next = fake_head2.next.next
        cur.next = None
        
        #self.reverse(fake_head2)
        cur = fake_head2
        while cur.next:
            cur = cur.next
        cur.next = fake_head1.next
        return fake_head2.next
        
    def reverse(self, root):
        left, mid, right = root.next, root.next.next, root.next.next.next
        while mid:
            mid.next = left
            left = mid
            mid = right
            if mid:
                right = mid.next
        root.next.next = None
        root.next = left
        return root
