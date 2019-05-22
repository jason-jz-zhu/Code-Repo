class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        # write your code here
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        up = [[0 for _ in range(n)] for _ in range(m)]
        down = [[0 for _ in range(n)] for _ in range(m)]
        left = [[0 for _ in range(n)] for _ in range(m)]
        right = [[0 for _ in range(n)] for _ in range(m)]

        # up
        for i in range(m):
            for j in range(n):
                up[i][j] = 0
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        up[i][j] += 1
                    if i > 0:
                        up[i][j] += up[i - 1][j]

        # down
        for i in range(m - 1, -1, -1):
            for j in range(n):
                down[i][j] = 0
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        down[i][j] += 1
                    if i + 1 < m:
                        down[i][j] += down[i + 1][j]

        # left
        for i in range(m):
            for j in range(n):
                left[i][j] = 0
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        left[i][j] += 1
                    if j > 0:
                        left[i][j] += left[i][j - 1]

        # right
        for i in range(m):
            for j in range(n - 1, -1, -1):
                right[i][j] = 0
                if grid[i][j] != 'W':
                    if grid[i][j] == 'E':
                        right[i][j] += 1
                    if j + 1 < n:
                        right[i][j] += right[i][j + 1]

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res = max(res, up[i][j] + down[i][j] + left[i][j] + right[i][j])

        return res
