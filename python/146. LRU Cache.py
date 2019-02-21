class Node:
    def __init__(self, key = None, value = None, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: 'int'):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: 'int') -> 'int':
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        # delete node
        node.prev.next = node.next
        node.next.prev = node.prev
        # move node to tail
        self.move_to_tail(node)
        return node.value

    def put(self, key: 'int', value: 'int') -> 'None':
        if self.get(key) != -1:
            self.hashmap[key].value = value
            return
        if len(self.hashmap) == self.capacity:
            del self.hashmap[self.head.next.key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

        new_node = Node(key, value)
        self.hashmap[key] = new_node
        self.move_to_tail(new_node)

    def move_to_tail(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
