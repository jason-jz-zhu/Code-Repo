class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals is None or len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key = lambda x: x[0])
        heap = []
        heapq.heappush(heap, intervals[0][1])

        for p in intervals[1:]:
            if p[0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, p[1])
        return len(heap)





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
