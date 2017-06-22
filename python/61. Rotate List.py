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
        if head is None:
            return None

        if k <= 0:
            return head

        p, n = head, 0
        # loop the list and count the length
        while p:
            n += 1
            if p.next is None:
                p.next = head
                break
            else:
                p = p.next

        actual_k = n - k % n
        for i in xrange(actual_k - 1):
            head = head.next
        tail = head
        head = head.next
        tail.next = None
        return head
