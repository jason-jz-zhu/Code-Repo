# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        sorted_intervals = sorted((interval.start, i) for i, interval in enumerate(intervals))
        res = []
        for interval in intervals:
            idx = bisect.bisect_left(sorted_intervals, (interval.end,))
            res.append(sorted_intervals[idx][1] if idx < len(sorted_intervals) else -1)
        return res
