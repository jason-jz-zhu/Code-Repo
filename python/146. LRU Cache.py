class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hashmap:
            return -1

        curr = self.hashmap[key]
        # delete current node
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        # update current to tail
        self.move_to_tail(curr)
        # return current
        return curr.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # if key in hash table
        if self.get(key) != -1:
            self.hashmap[key].value = value
            return
        # if reach the size of cap
        if len(self.hashmap) == self.capacity:
            del self.hashmap[self.head.next.key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        # update current to tail
        insert = Node(key, value)
        self.hashmap[key] = insert
        self.move_to_tail(insert)

    def move_to_tail(self, curr):
        curr.prev = self.tail.prev
        curr.next = self.tail
        self.tail.prev = curr
        curr.prev.next = curr


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
