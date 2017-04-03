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
        if head is None or head.next is None:
            return head
        mid = self.find_mid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        return self.merge_two_list(left, right)

    def find_mid(self, head):
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_two_list(self, head1, head2):
        dummay = ListNode(0)
        pre = dummay
        while head1 and head2:
            if head1.val < head2.val:
                pre.next = head1
                head1 = head1.next
            else:
                pre.next = head2
                head2 = head2.next
            pre = pre.next
        pre.next = head1 or head2
        return dummay.next
