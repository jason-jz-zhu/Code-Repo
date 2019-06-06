class Solution:
    def minCut(self, s: str) -> int:
        m = len(s)
        is_pal = [[False for _ in range(m)] for _ in range(m)]
        for i in range(m):
            is_pal[i][i] = True
        dp = [0 for _ in range(m)]

        for i in range(m - 1, -1, -1):
            dp[i] = m - i - 1
            for j in range(i, m):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

                    if j == m - 1:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], dp[j + 1] + 1)
        return dp[0]
