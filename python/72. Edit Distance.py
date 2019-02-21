class Solution:
    def minDistance(self, word1: 'str', word2: 'str') -> 'int':
        m, n = len(word1), len(word2)
        if m * n == 0:
            return m + n

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(m + 1):
            dp[0][j] = j
        for i in range(n + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = dp[i - 1][j]
                up = dp[i][j - 1]
                left_up = dp[i - 1][j - 1]
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = left_up
                else:
                    dp[i][j] = min(left, up, left_up) + 1
        return dp[n][m]
