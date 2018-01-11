# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        n, curr = 0, root
        while curr:
            curr = curr.next
            n += 1
        chunk_size, longer_chunks = n // k, n % k
        res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)
        prev, curr = None, root
        for idx, num in enumerate(res):
            if prev:
                prev.next = None
            res[idx] = curr
            for _ in range(num):
                prev, curr = curr, curr.next
        return res
