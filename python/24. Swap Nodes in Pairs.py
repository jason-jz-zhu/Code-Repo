# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next and curr.next.next:
            p1, p2 = curr.next, curr.next.next
            curr.next = p2
            p1.next = p2.next
            p2.next = p1
            curr = p1
        return dummy.next




class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        if not head:
            return None
        self.helper(head)
        return head

    def helper(self, curr):
        if not curr or not curr.next:
            return
        curr.val, curr.next.val = curr.next.val, curr.val
        self.helper(curr.next.next)
        
