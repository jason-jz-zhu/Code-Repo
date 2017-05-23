class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return
        row_len = len(matrix)
        col_len = len(matrix[0])
        # init first row and column check
        f_row_check = f_col_check = False
        # check first column
        for i in xrange(row_len):
            if matrix[i][0] == 0:
                f_col_check = True
                break
        # check first row
        for i in xrange(col_len):
            if matrix[0][i] == 0:
                f_row_check = True
                break
        # scan matrix, find 0 and set corr col and row
        for i in xrange(1, row_len):
            for j in xrange(1, col_len):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        # set zero based on first col and row
        for i in xrange(1, row_len):
            for j in xrange(1, col_len):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        # deal with first col and row
        if f_row_check:
            for i in xrange(col_len):
                matrix[0][i] = 0

        if f_col_check:
            for i in xrange(row_len):
                matrix[i][0] = 0
