class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    res += 1
        return res

    def bfs(self, grid, i, j):
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        q = collections.deque([(i, j)])
        grid[i][j] = '2'
        while q:
            grid_x, grid_y = q.popleft()
            for k in range(4):
                x, y = grid_x + dx[k], grid_y + dy[k]
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                    continue
                if grid[x][y] == '1':
                    q.append((x, y))
                    grid[x][y] = '2'


# dfs
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0
        if grid[0] is None or len(grid[0]) == 0:
            return 0

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    res += 1
        return res

    def dfs(self, grid, i, j):
        dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
        grid[i][j] = '2'
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                continue
            if grid[x][y] == '1':
                self.dfs(grid, x, y)
