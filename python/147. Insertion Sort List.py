# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def isSorted(head):
            curr = head
            while curr and curr.next:
                if curr.val > curr.next.val:
                    return False
                curr = curr.next
            return True

        if head is None or isSorted(head):
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr, sorted_tail = head.next, head
        while curr:
            prev = dummy
            while prev.next.val < curr.val:
                prev = prev.next

            if prev == sorted_tail:
                curr, sorted_tail = curr.next, curr
            else:
                curr.next, prev.next, sorted_tail.next = prev.next, curr, curr.next
                curr = sorted_tail.next
        return dummy.next
