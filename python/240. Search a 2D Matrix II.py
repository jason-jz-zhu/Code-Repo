class Solution(object):
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

        x, y = 0, len(matrix[0]) - 1
        while x < len(matrix) and y >= 0:
            item = matrix[x][y]
            if item == target:
                return True
            elif item < target:
                x += 1
            else:
                y -= 1

        return False
