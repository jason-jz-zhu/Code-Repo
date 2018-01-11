# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        prev = None
        while head2:
            tmp = head2.next
            head2.next = prev
            prev = head2
            head2 = tmp
        curr1, curr2 = head, prev
        while curr2:
            next1, next2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = next1
            curr1, curr2 = next1, next2
