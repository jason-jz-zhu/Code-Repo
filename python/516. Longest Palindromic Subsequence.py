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


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        m = len(s)
        memo = [[-1 for _ in range(m)] for _ in range(m)]
        return self.dfs(s, 0, m - 1, memo)

    def dfs(self, s, i, j, memo):
        if memo[i][j] != -1:
            return memo[i][j]
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            memo[i][j] = self.dfs(s, i + 1, j - 1, memo) + 2
        else:
            memo[i][j] = max(self.dfs(s, i, j - 1, memo), self.dfs(s, i + 1, j, memo))
        return memo[i][j]
        
