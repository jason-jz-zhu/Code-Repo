class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_l_heap = []
        self.min_r_heap = []


    def addNum(self, num: int) -> None:
        small, large = self.max_l_heap, self.min_r_heap
        heapq.heappush(small, -num)
        left_max = heapq.heappop(small)
        heapq.heappush(large, -left_max)
        if len(small) < len(large):
            heapq.heappush(small, -heapq.heappop(large))



    def findMedian(self) -> float:
        small, large = self.max_l_heap, self.min_r_heap
        if len(small) > len(large):
            return -small[0]
        return (-small[0] + large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
