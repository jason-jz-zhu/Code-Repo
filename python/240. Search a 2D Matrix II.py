class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0:
            return False
        if matrix[0] is None or len(matrix[0]) ==0:
            return False

        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            tmp = matrix[row][col]
            if tmp == target:
                return True
            elif tmp < target:
                row += 1
            else:
                col -= 1
        return False
