class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        if timePoints is None or len(timePoints) == 0:
            return 0

        minutes = map(lambda x: int(x[: 2]) * 60 + int(x[3:]), timePoints)
        minutes.sort()
        res = sys.maxint
        for i in range(1, len(minutes)):
            diff = abs(minutes[i] - minutes[i - 1])
            res = min(res, diff)
        return min(res, 24 * 60 + minutes[0] - minutes[-1])
