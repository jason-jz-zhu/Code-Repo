class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return
        row_len = len(matrix)
        col_len = len(matrix[0])

        f_row_check = f_col_check = False

        for i in range(row_len):
            if matrix[i][0] == 0:
                f_col_check = True
                break
        for j in range(col_len):
            if matrix[0][j] == 0:
                f_row_check = True

        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, row_len):
            for j in range(1, col_len):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if f_row_check:
            for j in range(col_len):
                matrix[0][j] = 0

        if f_col_check:
            for i in range(row_len):
                matrix[i][0] = 0
