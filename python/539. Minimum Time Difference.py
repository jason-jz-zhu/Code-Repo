class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = map(lambda x: int(x[: 2]) * 60 + int(x[3:]), timePoints)
        minutes.sort()
        res = sys.maxint
        for i in xrange(1, len(minutes)):
            diff = abs(minutes[i] - minutes[i - 1])
            res = min(res, diff)
        return min(res, 1440 + minutes[0] - minutes[-1])
        
