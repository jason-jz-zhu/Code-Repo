class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = []
        m, n = len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                heapq.heappush(heap, matrix[i][j])
        res = 0
        for _ in xrange(k):
            res = heapq.heappop(heap)
        return res

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        heap = [(matrix[0][0], 0, 0)]
        res = None
        visited[0][0] = True
        for _ in xrange(k):
            res, i, j = heapq.heappop(heap)
            if i + 1 < m and not visited[i + 1][j]:
                visited[i + 1][j] = True
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n and not visited[i][j + 1]:
                visited[i][j + 1] = True
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return res


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        heap = [(matrix[0][0], 0, 0)]
        res = None
        for _ in xrange(k):
            res, i, j = heapq.heappop(heap)
            if i + 1 < m and j == 0:
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return res

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            mid = (lo + hi) >> 1
            loc = self.countLower(matrix, mid)
            if loc >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def countLower(self, matrix, num):
        i, j = len(matrix) - 1, 0
        cnt = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] <= num:
                cnt += i + 1
                j += 1
            else:
                i -= 1
        return cnt
