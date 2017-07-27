# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals is None or len(intervals) == 0:
            return []

        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        res = [sorted_intervals[0]]

        for i in xrange(1, len(sorted_intervals)):
            if sorted_intervals[i].start > res[-1].end:
                res.append(sorted_intervals[i])
            else:
                res[-1].end = res[-1].end if sorted_intervals[i].end < res[-1].end else sorted_intervals[i].end

        return res
        
