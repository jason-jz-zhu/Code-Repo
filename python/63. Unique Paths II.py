class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(2)]
        now, old = 0, 1
        for i in range(m):
            now, old = old, now
            for j in range(n):
                if i == 0 and j == 0:
                    dp[now][0] = 1
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[now][j] = 0
                    continue
                dp[now][j] = 0
                if i > 0:
                    dp[now][j] += dp[old][j]
                if j > 0:
                    dp[now][j] += dp[now][j - 1]
        return dp[now][-1]
