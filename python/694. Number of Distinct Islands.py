class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        shapes = set([])
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    shape = self.bfs(grid, i, j)
                    shapes.add(tuple(shape))
        return len(shapes)

    def bfs(self, grid, i, j):
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
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

class Solution:
    def numDistinctIslands(self, grid: 'List[List[int]]') -> 'int':
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
        dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
        grid[i][j] = 2
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                continue
            if grid[x][y] == 1:
                shape.append((x - i0, y - j0))
                self.dfs(grid, x, y, i0, j0, shape)
