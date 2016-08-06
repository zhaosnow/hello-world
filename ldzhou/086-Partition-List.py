# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 使用了快速排序的算法, 但是有点trick

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        fake_head = ListNode(0)
        fake_head.next = head
        j, i = fake_head, fake_head
        while i.next:
            if i.next.val < x:
                i_next = i.next
                i.next = i.next.next
                i_next.next = j.next
                j.next = i_next
                if i == j: #这个地方, 可能会出现 j 走在了i的前面的情况, 所以判断一下, j不能走到i的前面
                    i = i.next
                j = j.next
            else:
                i = i.next
        return fake_head.next


# 另外一个并不trick的方法, 使用两个链表分别保存小于x, 和大于等于x的节点, 这个比较好实现, 但是为啥没有想起来的呢?
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1, head2 = ListNode(0), ListNode(0)
        cur1, cur2 = head1, head2
        while head:
            if head.val < x:
                cur1.next = head
                cur1 = head
            else:
                cur2.next = head
                cur2 = head
            head = head.next
        cur2.next = None
        cur1.next = head2.next
        return head1.next
