class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []
        self._min = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._data.append(x)
        if len(self._min) == 0 or x <= self._min[-1]:
            self._min.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if len(self._min) > 0 and self._min[-1] == self._data[-1]:
            self._min.pop()
        if len(self._data) > 0:
            return self._data.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self._data) > 0:
            return self._data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self._min) > 0:
            return self._min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
