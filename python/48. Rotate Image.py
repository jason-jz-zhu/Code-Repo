class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return

        start, end = 0, len(matrix) - 1
        while start < end:
            for i in xrange(start, end):
                offset = i - start
                tmp = matrix[start][i]
                matrix[start][i] = matrix[end - offset][start]
                matrix[end - offset][start] = matrix[end][end - offset]
                matrix[end][end - offset] = matrix[start + offset][end]
                matrix[start+ offset][end] = tmp
            start += 1
            end -= 1


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return

        matrix.reverse()
        for i in xrange(len(matrix)):
            for j in xrange(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
