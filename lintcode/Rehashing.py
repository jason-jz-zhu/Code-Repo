"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        old_capacity = len(hashTable)
        # double the capacity
        self.new_capacity = old_capacity * 2
        self.res = [None for i in xrange(self.new_capacity)]
        # begin to scan the hashTable
        for item in hashTable:
            p = item
            while p is not None:
                self.add_node(p.val)
                # go to next
                p = p.next
        return self.res

    def add_node(self, value):
        key = self.hashcode(value, self.new_capacity)
        if self.res[key] is None:
            self.res[key] = ListNode(value)
        else:
            q = self.res[key]
            while q.next is not None:
                # go to next
                q = q.next
            q.next = ListNode(value)

    def hashcode(self, value, capacity):
        return value % capacity
