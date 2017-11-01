class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        import heapq
        if heightMap is None or len(heightMap) == 0 or len(heightMap[0]) == 0:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False for j in range(n)] for i in range(m)]

        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, [heightMap[i][j], i, j])
                    visited[i][j] = True

        dx, dy = [-1, 0, 0, 1], [0, 1, -1, 0]
        res = 0
        while heap:
            height, i, j = heapq.heappop(heap)
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    res += max(0, height - heightMap[x][y])
                    heapq.heappush(heap, [max(height, heightMap[x][y]), x, y])
                    visited[x][y] = True

        return res
