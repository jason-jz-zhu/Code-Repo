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
        if not head or not head.next:
            return head

        n, curr = 1, head
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = head

        curr, tail = head, curr
        for _ in xrange(n - k % n):
            tail = curr
            curr = curr.next
        tail.next = None

        return curr
