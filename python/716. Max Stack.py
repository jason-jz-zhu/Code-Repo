class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        print()
        maxVal = x if not self.stack else max(x, self.stack[-1][1])
        self.stack.append((x, maxVal))

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()[0]


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


    def popMax(self):
        """
        :rtype: int
        """
        maxVal = self.stack[-1][1]
        tmp = []
        while self.stack[-1][0] != maxVal:
            tmp.append(self.stack.pop())
        self.stack.pop()
        while tmp:
            self.push(tmp.pop()[0])
        return maxVal


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
