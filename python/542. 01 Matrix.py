# 2025
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[-1 for _ in range(n)] for _ in range(m)]

        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    res[i][j] = 0

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nextX, nextY = x + dx, y + dy
                if 0 <= nextX < m and 0 <= nextY < n and res[nextX][nextY] == -1:
                    q.append((nextX, nextY))
                    res[nextX][nextY] = res[x][y] + 1

        return res





class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        import collections
        q = collections.deque([])
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j] == 0:
                    q.append((i, j))
                else:
                    matrix[i][j] = float('inf')
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            cell = q.popleft()
            for dir in dirs:
                i, j = cell[0]+dir[0], cell[1]+dir[1]
                if not (0 <= i < len(matrix)) or not (0 <= j < len(matrix[0])) or \
                   matrix[i][j] <= matrix[cell[0]][cell[1]]+1:
                        continue
                q.append((i, j))
                matrix[i][j] = matrix[cell[0]][cell[1]]+1

        return matrix
