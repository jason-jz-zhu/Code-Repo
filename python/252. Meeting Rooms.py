# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if intervals is None:
            return False

        if len(intervals) == 0:
            return True

        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i].start < sorted_intervals[i - 1].end:
                return False
        return True
