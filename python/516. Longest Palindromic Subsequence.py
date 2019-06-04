# dp from right to left
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        if m == 0:
            return 0
        dp = [[0 for _ in range(m)] for _ in range(m)]
        for i in range(m - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, m):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][-1]



# dp length from 1 to m
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        if m == 0:
            return 0
        if m == 1:
            return 1

        dp = [[0 for _ in range(m)] for _ in range(m)]

        for i in range(m):
            dp[i][i] = 1

        for i in range(m - 1):
            dp[i][i + 1] = 2 if s[i] == s[i + 1] else 1

        for length in range(3, m + 1):
            for i in range(m - length + 1):
                j = i + length - 1
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                if s[i] == s[j]:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j -1] + 2)

        return dp[0][-1]
