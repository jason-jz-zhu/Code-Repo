class Node:
    def __init__(self, key = None, val = None, freq = 1, prev = None, next = None):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = prev
        self.next = next

class DLinkedList:
    def __init__(self):
        self._head = Node()
        self._tail = Node()
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size = 0

    def append(self, node):
        f_node = self._tail.prev
        f_node.next = node
        node.prev = f_node
        node.next = self._tail
        self._tail.prev = node
        self._size += 1


    def pop(self, node = None):
        if self._size == 0:
            return
        if not node:
            node = self._head.next
        f_node = node.prev
        f_node.next = node.next
        node.next.prev = f_node
        self._size -= 1
        return node

    def empty(self):
        return True if self._size == 0 else False


class LFUCache:
    def __init__(self, capacity):

        self._size = 0
        self._capacity = capacity

        self._node = dict() # key: Node
        self._freq = collections.defaultdict(DLinkedList)
        self._minfreq = 0


    def _update(self, node):

        freq = node.freq

        self._freq[freq].pop(node)
        if self._minfreq == freq and self._freq[freq].empty():
            self._minfreq += 1

        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)

    def get(self, key):

        if key not in self._node:
            return -1

        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key, value):

        if self._capacity == 0:
            return

        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._minfreq].pop()
                print(node)
                del self._node[node.key]
                self._size -= 1

            node = Node(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._minfreq = 1
            self._size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
