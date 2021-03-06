# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        import heapq
        if intervals is None or len(intervals) == 0:
            return 0
        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        heap = []
        heapq.heappush(heap, sorted_intervals[0].end)
        for i in xrange(1, len(sorted_intervals)):
            if heap[0] <= sorted_intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap, sorted_intervals[i].end)

        return len(heap)


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        start, end = [], []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
            start.sort()
            end.sort()

        res = endpos = 0
        for i in xrange(len(intervals)):
            if start[i] < end[endpos]:
                res += 1
            else:
                endpos += 1
        return res
