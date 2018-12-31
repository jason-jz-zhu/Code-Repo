class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        sum_ = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # padding sum_ to make sum calculation easier
        for i in range(1, m+1):
            for j in range(1, n+1):
                sum_[i][j] = sum_[i][j-1] + sum_[i-1][j] - sum_[i-1][j-1] + matrix[i-1][j-1]
        self.sum_ = sum_

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sum_[row2 + 1][col2 + 1] - self.sum_[row1][col2 + 1] - self.sum_[row2 + 1][col1] + self.sum_[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
