class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        island = 0

        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == '1':
                    self.markbyBFS(grid, i, j)
                    island += 1
        return island

    def markbyBFS(self, grid, i, j):
        dir_x, dir_y = [0, 1, -1, 0],  [1, 0, 0, -1]
        q = collections.deque([(i, j)])
        grid[i][j] = '0'
        while q:
            x, y = q.popleft()
            for k in xrange(4):
                grid_x, grid_y = x + dir_x[k], y + dir_y[k]
                if grid_x < 0 or grid_x >= len(grid) or grid_y < 0 or grid_y >= len(grid[0]):
                    continue
                if grid[grid_x][grid_y] == '1':
                    grid[grid_x][grid_y] = '0'
                    q.append((grid_x, grid_y))




class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = 0
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                return 1
            return 0
        return sum(sink(i, j) for i in xrange(len(grid)) for j in xrange(len(grid[i])))
