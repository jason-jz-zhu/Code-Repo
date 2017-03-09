# binary search twice
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if matrix is None or len(matrix) == 0:
            return False
        if matrix[0] is None or len(matrix[0]) == 0:
            return False
        # write your code here
        start, end = 0, len(matrix) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        result = []
        if matrix[end][0] == target:
            return True
        elif matrix[end][0] < target:
            result = matrix[end]
        else:
            result = matrix[start]

        start, end = 0, len(result) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if result[mid] == target:
                return True
            if result[mid] < target:
                start = mid
            else:
                end = mid
        if result[start] == target or result[end] == target:
            return True
        return False

# binary search once
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if matrix is None or len(matrix) == 0:
            return False
        if matrix[0] is None or len(matrix[0]) == 0:
            return False
        # write your code here
        row, col = len(matrix), len(matrix[0])
        start, end = 0, (row * col) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            num = matrix[mid / col][mid % col]
            if num == target:
                return True
            elif num < target:
                start = mid
            else:
                end = mid
        if matrix[start / col][start % col] == target:
            return True
        elif matrix[end / col][end % col] == target:
            return True
        return False
