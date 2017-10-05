# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if intervals is None or len(intervals) == 0:
            return 0

        intervals.sort(key = lambda x: x.start)

        res = 0
        end = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < end:
                res += 1
                end = min(intervals[i].end, end)
            else:
                end = intervals[i].end
        return res
