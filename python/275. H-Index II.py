class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or len(citations) == 0:
            return 0

        n = len(citations)
        start, end = 0, n - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if citations[mid] >= n - mid:
                end = mid
            else:
                start = mid
        if citations[start] >= n - start:
            return n - start
        if citations[end] >= n - end:
            return n - end
        return n - end - 1
