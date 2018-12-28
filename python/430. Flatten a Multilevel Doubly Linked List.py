"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        curr = head
        while curr:
            if not curr.child:
                curr = curr.next
                continue
            child = curr.child
            childTail = child
            while childTail.next:
                childTail = childTail.next
            curr.child = None
            child.prev = curr
            childTail.next = curr.next
            if curr.next:
                curr.next.prev = childTail
            curr.next = child
            curr = curr.next
        return head
