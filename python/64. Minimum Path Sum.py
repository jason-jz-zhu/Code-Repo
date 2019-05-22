class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(2)]
        now, old = 0, 1
        for i in range(m):
            now, old = old, now
            for j in range(n):
                if i == 0 and j == 0:
                    dp[now][j] = grid[i][j]
                    continue
                dp[now][j] = float('inf')
                if i > 0:
                    dp[now][j] = min(dp[now][j], dp[old][j] + grid[i][j])
                if j > 0:
                    dp[now][j] = min(dp[now][j], dp[now][j - 1] + grid[i][j])
        return dp[now][-1]
