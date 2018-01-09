class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 1]
        for x in range(2, n + 1):
            dp.append(x * (dp[-1] + dp[-2]) % (10**9 + 7))
        return dp[n - 1]
