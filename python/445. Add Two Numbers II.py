# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        if l1 is None or l2 is None:
            return l1 if l1 is not None else l2

        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        prev = head = None
        carry = 0
        while stack1 or stack2 or carry:
            if stack1:
                carry += stack1.pop()
            if stack2:
                carry += stack2.pop()
            remainder = carry % 10
            carry /= 10
            head = ListNode(remainder)
            head.next = prev
            prev = head
        return head
