"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

import heapq

class Type:
    def __init__(self, val, node):
        self.val = val
        self.node = node

    def __cmp__(self, other):
        return self.val - other.val

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        # check edage case
        if lists is None or len(lists) == 0:
            return None
        # init heap
        heap = []
        for head in lists:
            if head is not None:
                heapq.heappush(heap, Type(head.val, head))

        # use point to walk
        dummy = ListNode(0)
        tail = dummy
        while len(heap) > 0:
            head = heapq.heappop(heap)
            tail.next = head.node
            tail = head.node
            if head.node.next:
                heapq.heappush(heap, Type(head.node.next.val, head.node.next))

        return dummy.next
