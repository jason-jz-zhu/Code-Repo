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
        if intervals is None or len(intervals) == 0:
            return 0
        sorted_intervals = sorted(intervals, key = lambda x: x.start)
        heap = []
        heapq.heappush(heap, sorted_intervals[0].end)
        for i in range(1, len(sorted_intervals)):
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
        if intervals is None or len(intervals) == 0:
            return 0

        start = sorted([s.start for s in intervals])
        end = sorted([s.end for s in intervals])

        res = endpos = 0
        for i in range(len(intervals)):
            if start[i] < end[endpos]:
                res += 1
            else:
                endpos += 1
        return res
