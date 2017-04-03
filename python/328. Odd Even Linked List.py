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
        if not head or not head.next:
            return head
        pre, cur = head, head.next
        while cur and cur.next:
            temp = pre.next
            pre.next = cur.next
            cur.next = cur.next.next
            pre.next.next = temp
            cur = cur.next
            pre = pre.next
        return head
