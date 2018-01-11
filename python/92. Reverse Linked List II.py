class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        for _ in range(m - 1):
            head = head.next
        prev = head.next
        curr = prev.next
        for _ in range(n - m):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head.next.next = curr
        head.next = prev
        return dummy.next
