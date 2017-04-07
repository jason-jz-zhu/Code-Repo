class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = [[1 for i in xrange(n)] for j in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                res[i][j] = res[i-1][j] + res[i][j-1]

        return res[-1][-1]
