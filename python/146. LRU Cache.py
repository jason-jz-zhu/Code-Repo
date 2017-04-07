class Node:
    def __init__(self, key=None, value=None, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.hash = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.hash.get(key) is None:
            return -1
        current = self.hash.get(key)
        # delete current node
        current.pre.next = current.next
        current.next.pre = current.pre
        # update current to tail
        self.move_to_tail(current)
        # return current
        return self.hash.get(key).value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # if key not in hash table
        if self.get(key) != -1:
            self.hash.get(key).value = value
            return
        # if reach the size of cap
        if len(self.hash) == self.cap:
            del self.hash[self.head.next.key]
            self.head.next = self.head.next.next
            self.head.next.pre = self.head
        # update current to tail
        insert = Node(key, value)
        self.hash[key] = insert
        self.move_to_tail(insert)

    def move_to_tail(self, current):
        current.pre = self.tail.pre
        current.next = self.tail
        self.tail.pre = current
        current.pre.next = current


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
