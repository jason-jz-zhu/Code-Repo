# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals is None or len(intervals) == 0:
            return [newInterval]
        if newInterval is None or len(intervals) == 0:
            return intervals

        res = []
        point = 0
        for pair in intervals:
            if newInterval.start > pair.end:
                res.append(pair)
                point += 1
            elif newInterval.end < pair.start:
                res.append(pair)
            else:
                newInterval.start = min(newInterval.start, pair.start)
                newInterval.end = max(newInterval.end, pair.end)
        res.insert(point, newInterval)
        return res
        
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals is None or len(intervals) == 0:
            return [newInterval]
        if newInterval is None or len(intervals) == 0:
            return intervals

        intervals.append(newInterval)
        intervals.sort(key = lambda x: x.start)
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1].end < intervals[i].start:
                res.append(intervals[i])
            else:
                res[-1].end = res[-1].end if intervals[i].end < res[-1].end else intervals[i].end
        return res
