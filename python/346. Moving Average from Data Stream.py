class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.s = 0
        self.size = size
        self.queue = collections.deque([])

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) == self.size:
            left = self.queue.popleft()
            self.s -= left

        self.queue.append(val)
        self.s += val
        return self.s / len(self.queue)




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
