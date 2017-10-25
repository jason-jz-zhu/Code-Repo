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

# TLE 
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
        # check horizontal
        for i in range(m):
            cnt = 0
            for j in range(n):
                if M[i][j] == 1:
                    cnt += 1
                    res = max(res, cnt)
                else:
                    cnt = 0
        # check vertical
        for j in range(n):
            cnt = 0
            for i in range(m):
                if M[i][j] == 1:
                    cnt += 1
                    res = max(res, cnt)
                else:
                    cnt = 0
        for i in range(m + n - 1):
            cnt1 = cnt2 = 0
            # check diagonal
            for j in range(i, -1, -1):
                if i - j < m and j < n:
                    if M[i - j][j] == 1:
                        cnt1 += 1
                        res = max(res, cnt1)
                    else:
                        cnt1 = 0
                # check anti-diagonal
                t = m - 1 - i + j
                if t >= 0 and t < m and j < n:
                    if M[t][j] == 1:
                        cnt2 += 1
                        res = max(res, cnt2)
                        print res
                    else:
                        cnt2 = 0
        return res
