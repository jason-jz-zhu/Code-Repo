class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._times = [0] * 300
        self._hits = [0] * 300


    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = timestamp % 300
        if self._times[idx] != timestamp:
            self._times[idx] = timestamp
            self._hits[idx] = 1
        else:
            self._hits[idx] += 1


    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        res = 0
        for i in range(300):
            if timestamp - self._times[i] < 300:
                res += self._hits[i]
        return res



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
