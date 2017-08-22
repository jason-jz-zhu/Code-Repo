# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        fast, slow = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        head1, head2=head, slow.next
        slow.next, pre=None, None
        while head2:
            tmp = head2.next
            head2.next = pre
            pre, head2 = head2, tmp

        cur1, cur2=head1, pre
        while cur2:
            next1, next2=cur1.next, cur2.next
            cur1.next=cur2
            cur2.next=next1
            cur1, cur2=next1, next2
