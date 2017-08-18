class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        qp = collections.deque([])
        qa = collections.deque([])
        mp = [[False for _ in xrange(n)] for _ in xrange(m)]
        ma = [[False for _ in xrange(n)] for _ in xrange(m)]
        res = []
        for i in xrange(m):
            qp.append((i, 0))
            qa.append((i, n - 1))
            mp[i][0] = True
            ma[i][n - 1] = True
        for j in xrange(n):
            qp.append((0, j))
            qa.append((m - 1, j))
            mp[0][j] = True
            ma[m - 1][j] = True

        self.bfs(matrix, mp, qp)
        self.bfs(matrix, ma, qa)

        for i in xrange(m):
            for j in xrange(n):
                if mp[i][j] and ma[i][j]:
                    res.append([i, j])
        return res

    def bfs(self, matrix, visited, q):
        m, n = len(matrix), len(matrix[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            curr_x, curr_y = q.popleft()
            for d in dirs:
                x, y = curr_x + d[0], curr_y + d[1]
                if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[curr_x][curr_y]:
                    continue
                visited[x][y] = True
                q.append((x, y))

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(matrix)
        n = len(matrix[0])
        p_visited = [[False for _ in range(n)] for _ in range(m)]

        a_visited = [[False for _ in range(n)] for _ in range(m)]
        result = []

        for i in range(m):
            # p_visited[i][0] = True
            # a_visited[i][n-1] = True
            self.dfs(matrix, i, 0, p_visited, m, n)
            self.dfs(matrix, i, n-1, a_visited, m, n)
        for j in range(n):
            # p_visited[0][j] = True
            # a_visited[m-1][j] = True
            self.dfs(matrix, 0, j, p_visited, m, n)
            self.dfs(matrix, m-1, j, a_visited, m, n)

        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i,j])
        return result


    def dfs(self, matrix, i, j, visited, m, n):
        # when dfs called, meaning its caller already verified this point
        visited[i][j] = True
        for dir in self.directions:
            x, y = i + dir[0], j + dir[1]
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, x, y, visited, m, n)
