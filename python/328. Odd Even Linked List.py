# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        odd_tail, curr = head, head.next
        while curr and curr.next:
            even_head = odd_tail.next
            odd_tail.next = curr.next
            odd_tail = odd_tail.next
            curr.next = odd_tail.next
            odd_tail.next = even_head
            curr = curr.next
        return head
