class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0:
            return []

        matrix = [[0 for i in xrange(n)] for j in xrange(n)]

        up, left, down, right = 0, 0, n -1, n - 1
        direct = 0
        count = 0
        while True:
            if direct == 0:
                for i in xrange(left, right + 1):
                    count += 1
                    matrix[up][i] = count
                up += 1
            if direct == 1:
                for i in xrange(up, down + 1):
                    count += 1
                    matrix[i][right] = count
                right -= 1
            if direct == 2:
                for i in xrange(right, left - 1, -1):
                    count += 1
                    matrix[down][i] = count
                down -= 1
            if direct == 3:
                for i in xrange(down, up - 1, -1):
                    count += 1
                    matrix[i][left] = count
                left += 1
            if count == n * n:
                return matrix
            direct = (direct + 1) % 4