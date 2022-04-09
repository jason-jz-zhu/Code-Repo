# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
    
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        return self.reverse(head)

    def reverse(self, node, prev=None):
        if not node:
            return prev
        tmp = node.next
        node.next = prev
        return self.reverse(tmp, node)
