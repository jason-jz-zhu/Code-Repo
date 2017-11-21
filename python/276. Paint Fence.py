class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        elif n == 2:
            return k * k

        dp = [k, k * k, 0]

        for i in range(2, n):
            dp[2] = (k - 1) * (dp[0] + dp[1])
            dp[0] = dp [1]
            dp[1] = dp[2]

        return dp[2]
