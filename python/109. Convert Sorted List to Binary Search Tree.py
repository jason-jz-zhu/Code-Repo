# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def helper(head, tail):
            slow, fast = head, head
            if head == tail:
                return None
            while fast != tail and fast.next != tail:
                fast = fast.next.next
                slow = slow.next
            cur = TreeNode(slow.val)
            cur.left = helper(head, slow)
            cur.right = helper(slow.next, tail)
            return cur
        
        if not head:
            return None
        return helper(head, None)







class Solution(object):
    def sortedListToBST(self, head):
        cur, l = head, 0
        while cur:
            cur, l = cur.next, l + 1
        self.head = head
        return self.helper(0, l)

    def helper(self, start, end):
        if start == end:
            return None
        mid = start + (end - start) / 2
        left = self.helper(start, mid)
        cur = TreeNode(self.head.val)
        cur.left = left
        self.head = self.head.next
        cur.right = self.helper(mid + 1, end)
        return cur
