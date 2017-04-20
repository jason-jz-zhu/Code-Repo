# space O(n*n/2) and top to bottom
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle is None or len(triangle) == 0 or len(triangle[0]) == 0:
            return -1
        n = len(triangle)
        dp = [[0 for i in xrange(len(row))] for row in triangle]
        dp[0][0] = triangle[0][0]
        for i in xrange(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        # top to down
        for i in xrange(1, n):
            for j in xrange(1, i):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

        return min(dp[-1])

# space O(n) and bottom to top
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle is None or len(triangle) == 0 or len(triangle[0]) == 0:
            return -1
        n = len(triangle)
        dp = triangle[-1]
        for i in xrange(n-2, -1, -1):
            for j in xrange(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]
