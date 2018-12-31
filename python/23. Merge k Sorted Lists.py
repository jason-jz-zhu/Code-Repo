# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Type:
    def __init__(self, val, node):
        self.val = val
        self.node = node
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, Type(l.val, l))
        while heap:
            tmp = heapq.heappop(heap)
            val = tmp.val
            node = tmp.node
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            if node:
                heapq.heappush(heap, Type(node.val, node))
        return dummy.next
