class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        row, column = len(grid), len(grid[0])
        # init all to 0
        dp = [[0 for i in xrange(column)] for j in xrange(row)]
        # init left top point
        dp[0][0] = grid[0][0]
        # init first row
        for r in xrange(1, row):
            dp[r][0] = dp[r-1][0] + grid[r][0]
        # init first column
        for c in xrange(1, column):
            dp[0][c] = dp[0][c-1] + grid[0][c]
        # function & calcuation
        for i in xrange(1, row):
            for j in xrange(1, column):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[-1][-1]
