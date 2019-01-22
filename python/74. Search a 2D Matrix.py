class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0:
            return False
        if matrix[0] is None or len(matrix[0]) == 0:
            return False

        row, col = len(matrix), len(matrix[0])
        start, end = 0, row * col - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            tmp = matrix[mid // col][mid % col]
            if tmp == target:
                return True
            elif tmp < target:
                start = mid
            else:
                end = mid
        if matrix[start // col][start % col] == target:
            return True
        elif matrix[end // col][end % col] == target:
            return True
        return False
