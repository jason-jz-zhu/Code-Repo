class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, self.bfs(grid, i, j))
        return res

    def bfs(self, grid, i, j):
        res = 0
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        q = collections.deque([(i, j)])
        grid[i][j] = 2
        while q:
            grid_x, grid_y = q.popleft()
            res += 1
            for k in range(4):
                x, y = grid_x + dx[k], grid_y + dy[k]
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                    continue
                if grid[x][y] == 1:
                    grid[x][y] = 2
                    q.append((x, y))
        return res
