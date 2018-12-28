# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge(left, right)

    def findMid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, head1, head2):
        dummy = ListNode(0)
        prev = dummy
        while head1 and head2:
            if head1.val < head2.val:
                prev.next = head1
                head1 = head1.next
            else:
                prev.next = head2
                head2 = head2.next
            prev = prev.next
        prev.next = head1 or head2
        return dummy.next
