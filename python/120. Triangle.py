class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle is None or len(triangle) == 0 or len(triangle[0]) == 0:
            return sys.maxint

        dp = [[0 for _ in range(len(row))] for row in triangle]
        dp[0][0] = triangle[0][0]

        for i in range(1, len(triangle)):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        for i in range(2, len(triangle)):
            for j in range(1, i):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

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
