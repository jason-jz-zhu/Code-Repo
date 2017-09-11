class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2 or n == 3:
            return n - 1
        if n == 4:
            return n
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0, 0, 1, 2, 4, 6, 9]
        for i in xrange(7, n + 1):
            dp.append(3 * dp[i - 3])
        return dp[n]
        
