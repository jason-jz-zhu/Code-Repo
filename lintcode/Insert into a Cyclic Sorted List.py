"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    # @param {ListNode} node a list node in the list
    # @param {int} x an integer
    # @return {ListNode} the inserted new list node
    def insert(self, node, x):
        # Write your code here
        if node is None:
            new_node = ListNode(x)
            new_node.next = new_node
            return new_node

        pre = None
        cur = node
        while True:
            pre = cur
            cur = cur.next
            if pre.val <= x and x <= cur.val:
                break
            if pre.val > cur.val and (pre.val < x or cur.val > x):
                break
            if cur is node:
                break

        new_node = ListNode(x)
        new_node.next = cur
        pre.next = new_node
        return new_node
