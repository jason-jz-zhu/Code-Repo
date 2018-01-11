# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        n, curr = 1, head
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = head
        for _ in range(n - k % n):
            curr = curr.next
        head = curr.next
        curr.next = None
        return head
