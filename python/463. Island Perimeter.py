class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        res = 0
        # main loop
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                # left side
                if j == 0 or grid[i][j - 1] == 0:
                    res += 1
                # top side
                if i == 0 or grid[i - 1][j] == 0:
                    res += 1
                # right side
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    res += 1
                # bottom side
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    res += 1
        return res
