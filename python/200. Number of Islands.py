# bfs
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
                    self.bfs(grid, i, j)
                    res += 1
        return res

    def bfs(self, grid, i, j):
        dir_x, dir_y = [-1, 0, 0, 1], [0, 1, -1, 0]
        q = collections.deque([(i, j)])
        grid[i][j] = '2'
        while q:
            x, y = q.popleft()
            for k in range(4):
                grid_x, grid_y = x + dir_x[k], y + dir_y[k]
                if grid_x < 0 or grid_x >= len(grid) or grid_y < 0 or grid_y >= len(grid[0]):
                    continue
                if grid[grid_x][grid_y] == '1':
                    grid[grid_x][grid_y] = '2'
                    q.append((grid_x, grid_y))


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
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == '1':
            grid[i][j] = '2'
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)
