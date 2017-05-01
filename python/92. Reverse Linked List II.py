# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        for _ in xrange(m - 1):
            head = head.next
        pre = head.next
        cur = pre.next
        for _ in xrange(n - m):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        head.next.next = cur
        head.next = pre
        return dummy.next
