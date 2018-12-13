class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))


    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heaps
        if len(large) > len(small):
            return large[0]
        return (-small[0] + large[0]) / 2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
