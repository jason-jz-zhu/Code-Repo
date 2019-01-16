class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1:
            return 0
        f = [[0 for _ in range(n)] for _ in range(m)]
        # init
        f[0][0] = 1
        for i in range(1, m):
            f[i][0] = 1
        for j in range(1, n):
            f[0][j] = 1

        # tf
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]

        return f[-1][-1]
