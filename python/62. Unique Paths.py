class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(2)]
        now, old = 0, 1
        for i in range(m):
            now, old = old, now
            for j in range(n):
                if i == 0 and j == 0:
                    dp[now][0] = 1
                    continue
                dp[now][j] = 0
                if i > 0:
                    dp[now][j] += dp[old][j]
                if j > 0:
                    dp[now][j] += dp[now][j - 1]
        return dp[now][-1]
