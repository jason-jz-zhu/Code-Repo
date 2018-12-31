"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            head = Node(insertVal, None)
            head.next = head
            return head
        curr = head
        while curr.next != head:
            if curr.val <= insertVal and curr.next.val >= insertVal:
                break
            if curr.val > curr.next.val and (curr.val <= insertVal or curr.next.val >= insertVal):
                break
            curr = curr.next
        newNode = Node(insertVal, curr.next)
        curr.next = newNode
        return head

        
