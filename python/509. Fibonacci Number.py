class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        dp = [0] * (N + 1)
        dp[1] = 1
        for i in range(2, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        a = 0
        b = 1
        for i in range(2, N + 1):
            tmp = a + b
            a = b
            b = tmp
        return b
