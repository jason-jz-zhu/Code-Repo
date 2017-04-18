# O(n) and bottom up
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in xrange(n+1)]
        dp[0], dp[1] = 1, 1
        for i in xrange(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

# O(1) and bottom up
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        a, b = 1, 1
        now = 0
        for i in xrange(2, n+1):
            a, b = b, a + b
        return b
