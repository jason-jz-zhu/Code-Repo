# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# use hash table and O(n), scan once
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        hash = {}
        dummy = RandomListNode(0)
        pre = dummy
        while head:
            if head in hash:
                new_node = hash[head]
            else:
                new_node = RandomListNode(head.label)
                hash[head] = new_node
            pre.next = new_node

            if head.random is not None:
                if head.random in hash:
                    new_node.random = hash[head.random]
                else:
                    new_node.random = RandomListNode(head.random.label)
                    hash[head.random] = new_node.random
            pre = new_node
            head = head.next
        return dummy.next

# use hash table and O(n), scan twice
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        hash = {}
        dummy = RandomListNode(0)
        pre = dummy
        # the first scan to deep copy nodes and copy random
        while head:
            # deep copy for label
            new_node = RandomListNode(head.label)
            pre.next = new_node
            # append old for key and new for value
            hash[head] = new_node
            # copy for random
            new_node.random = head.random
            # move to next node
            pre = pre.next
            head = head.next

        # the second scan to deep copy random
        head = dummy.next
        while head:
            if head.random:
                head.random = hash[head.random]
            head = head.next
        return dummy.next

# not use hash table and O(n), scan three times
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        dummy = RandomListNode(0)
        dummy.next = head
        # copy new node and append it to old node
        while head:
            new_node = RandomListNode(head.label)
            new_node.next = head.next
            head.next = new_node
            head = head.next.next
        # copy random node
        head = dummy.next
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next
        # split old and new
        new_head = dummy.next.next
        head = dummy.next
        while head:
            new_node = head.next
            head.next = head.next.next
            if new_node.next:
                new_node.next = new_node.next.next
            head = head.next
        return new_head
