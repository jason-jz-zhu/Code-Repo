# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        fast, slow = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        head2, pre = slow.next, None

        while head2:
            tmp = head2.next
            head2.next = pre
            pre = head2
            head2 = tmp

        p1, p2 = pre, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next
        return p1 is None
