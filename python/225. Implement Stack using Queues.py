class MyStack(object):
    import collections
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._q = collections.deque()
        self._top = None


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self._q.append(x)
        self._top = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for _ in range(len(self._q) - 1):
            self._top = self._q.popleft()
            self._q.append(self._top)
        return self._q.popleft()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self._top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self._q) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()







class Queue:
    def __init__(self):
        self.data = collections.deque()

    def push(self, x):
        self.data.append(x)

    def peek(self):
        return self.data[0]

    def pop(self):
        return self.data.popleft()

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

class MyStack(object):
    # initialize your data structure here.
    def __init__(self):
        self.q_ = Queue()
        self.top_ = None

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q_.push(x)
        self.top_ = x

    # @return nothing
    def pop(self):
        for _ in xrange(self.q_.size() - 1):
            self.top_ = self.q_.pop()
            self.q_.push(self.top_)
        return self.q_.pop()

    # @return an integer
    def top(self):
        return self.top_

    # @return an boolean
    def empty(self):
        return self.q_.empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
