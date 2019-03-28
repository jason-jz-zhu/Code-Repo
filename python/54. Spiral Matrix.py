class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        res = []
        up, left, down, right = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        direction = 0 #  0 -> go right, 1 -> go down, 2 -> go left, 3 -> go up
        while True:
            if direction == 0:
                for j in range(left, right + 1):
                    res.append(matrix[up][j])
                up += 1
            if direction == 1:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1
            if direction == 2:
                for j in range(right, left - 1, -1):
                    res.append(matrix[down][j])
                down -= 1
            if direction == 3:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            if up > down or left > right:
                return res
            direction = (direction + 1) % 4
        return res
