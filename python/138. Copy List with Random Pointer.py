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
        map = {}
        dummay = RandomListNode(0)
        pre = dummay
        while head:
            if head in map:
                new_node = map[head]
            else:
                new_node = RandomListNode(head.label)
                map[head] = new_node
            pre.next = new_node

            if head.random is not None:
                if head.random in map:
                    new_node.random = map[head.random]
                else:
                    new_node.random = RandomListNode(head.random.label)
                    map[head.random] = new_node.random
            pre = new_node
            head = head.next
        return dummay.next

            
