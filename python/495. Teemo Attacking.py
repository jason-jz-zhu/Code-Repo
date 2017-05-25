class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if timeSeries is None or len(timeSeries) == 0:
            return 0
        if duration <= 0:
            return 0
        if len(timeSeries) == 1:
            return duration
        res = 0
        timeP = timeSeries[0] + duration - 1
        for i in xrange(1, len(timeSeries)):
            if timeSeries[i] > timeP:
                res += duration
            else:
                res += (timeSeries[i] - timeSeries[i - 1])
            timeP = timeSeries[i] + duration - 1
        res += duration
        return res
