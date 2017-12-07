# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        hashmap = {}
        dummy = RandomListNode(0)
        prev = dummy
        while head:
            if head in hashmap:
                new_node = hashmap[head]
            else:
                new_node = RandomListNode(head.label)
                hashmap[head] = new_node

            if head.random is not None:
                if head.random in hashmap:
                    new_node.random = hashmap[head.random]
                else:
                    new_node.random = RandomListNode(head.random.label)
                    hashmap[head.random] = new_node.random
            prev.next = new_node
            prev = new_node
            head = head.next
        return dummy.next
