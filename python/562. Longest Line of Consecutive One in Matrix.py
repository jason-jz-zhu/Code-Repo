class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if M is None or len(M) == 0 or len(M[0]) == 0:
            return 0

        res = 0
        m, n = len(M), len(M[0])
        dp = [[[0] * 4 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if M[i][j] == 0:
                    continue
                for k in xrange(4):
                    dp[i][j][k] = 1
                if j > 0:
                    dp[i][j][0] += dp[i][j - 1][0]
                if i > 0:
                    dp[i][j][1] += dp[i - 1][j][1]
                if i > 0 and j < n - 1:
                    dp[i][j][2] += dp[i - 1][j + 1][2]
                if i > 0 and j > 0:
                    dp[i][j][3] += dp[i - 1][j - 1][3]
                res = max(res, dp[i][j][0], dp[i][j][1])
                res = max(res, dp[i][j][2], dp[i][j][3])
        return res
                    
