# dfs + Memoization
class Solution:
    def longestIncreasingPath(self, matrix: 'List[List[int]]') -> 'int':
        if matrix is None or len(matrix) == 0:
            return 0

        m, n = len(matrix), len(matrix[0])
        cache = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j, cache))
        return res

    def dfs(self, matrix, i, j, cache):
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        if cache[i][j] != 0:
            return cache[i][j]
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[i][j] >= matrix[x][y]:
                continue
            cache[i][j] = max(cache[i][j], self.dfs(matrix, x, y, cache))
        cache[i][j] += 1
        return cache[i][j]


# bfs - topo
class Solution:
    def longestIncreasingPath(self, matrix: 'List[List[int]]') -> 'int':
        if matrix is None or len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        indegree = [[0 for _ in range(n)] for _ in range(m)]
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        q = collections.deque([])
        for i in range(m):
            for j in range(n):
                for k in range(4):
                    next_x, next_y = i + dx[k], j + dy[k]
                    if 0 <= next_x < m and 0 <= next_y < n and matrix[i][j] > matrix[next_x][next_y]:
                        indegree[i][j] += 1
                if indegree[i][j] == 0:
                    q.append((i, j))

        res = 0
        while q:
            q_size = len(q)
            while q_size:
                q_size -= 1
                curr_x, curr_y = q.popleft()
                for k in range(4):
                    next_x, next_y = curr_x + dx[k], curr_y + dy[k]
                    if 0 <= next_x < m and 0 <= next_y < n and matrix[curr_x][curr_y] < matrix[next_x][next_y]:
                        indegree[next_x][next_y] -= 1
                        if indegree[next_x][next_y] == 0:
                            q.append((next_x, next_y))
            res += 1
        return res

            
