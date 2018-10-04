# O(n) and bottom up
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

# O(1) and bottom up
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 1, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

# Time complexity : O(n)
# Space complexity : O(n)
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        cache = [0] * (n + 1)
        return self.helper(0, n, cache)

    def helper(self, i, n, cache):
        if i > n:
            return 0
        if i == n:
            return 1
        if cache[i] > 0:
            return cache[i]
        cache[i] = self.helper(i + 1, n, cache) + self.helper(i + 2, n, cache)
        return cache[i]
