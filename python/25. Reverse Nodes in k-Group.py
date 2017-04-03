# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while True:
            head = self.reverse_k(head, k)
            if head is None:
                break
        return dummy.next

    def reverse_k(self, head, k):
        nk = head
        for i in xrange(k):
            if nk is None:
                return None
            nk = nk.next
        if nk is None:
            return None

        n1 = head.next
        nk_next = nk.next

        prev = None
        curt = n1
        while curt != nk_next:
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp

        head.next = nk
        n1.next = nk_next
        return n1
            
