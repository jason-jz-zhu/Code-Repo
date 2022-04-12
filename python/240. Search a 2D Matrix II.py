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

 class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        def search(left, up, right, down):
            if left > right or up > down:
                return False
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False
            
            mid = left + (right - left) // 2
            
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
                
            return search(left, row, mid - 1, down) or search(mid + 1, up, right, row - 1)
        
        
        return search(0, 0, len(matrix[0]) - 1, len(matrix) - 1)
