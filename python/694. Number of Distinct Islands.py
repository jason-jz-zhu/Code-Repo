class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    shape = self.bfs(grid, i, j)
                    res.add(tuple(shape))
        return len(res)

    def bfs(self, grid, i, j):
        dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
        q = collections.deque([(i, j)])
        grid[i][j] = 2
        shape = []
        while q:
            grid_x, grid_y = q.popleft()
            for k in range(4):
                x, y = grid_x + dx[k], grid_y + dy[k]
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                    continue
                if grid[x][y] == 1:
                    grid[x][y] = 2
                    q.append((x, y))
                    shape.append((x - i, y - j))
        return shape

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0
        if grid[0] is None or len(grid[0]) == 0:
            return 0

        res = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    shape = []
                    self.dfs(grid, i, j, i, j, shape)
                    res.add(tuple(shape))
        return len(res)

    def dfs(self, grid, i, j, i0, j0, shape):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == 1:
            grid[i][j] = 2
            shape.append((i - i0, j - j0))
            self.dfs(grid, i - 1, j, i0, j0, shape)
            self.dfs(grid, i + 1, j, i0, j0, shape)
            self.dfs(grid, i, j - 1, i0, j0, shape)
            self.dfs(grid, i, j + 1, i0, j0, shape)
