class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        res = 0
        # the first column
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            res = max(res, dp[i][0])
        # the first row
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            res = max(res, dp[0][j])
        # dp loop
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 if matrix[i][j] == '1' else 0
                res = max(res, dp[i][j])
        return res * res
            
