class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return []

        res =[[0 for _ in range(n)] for _ in range(n)]
        up, left, down, right = 0, 0, n - 1, n - 1
        direction = 0
        cnt = 0
        while True:
            if direction == 0:
                for j in range(left, right + 1):
                    cnt += 1
                    res[up][j] = cnt
                up += 1
            if direction == 1:
                for i in range(up, down + 1):
                    cnt += 1
                    res[i][right] = cnt
                right -= 1
            if direction == 2:
                for j in range(right, left - 1, -1):
                    cnt += 1
                    res[down][j] = cnt
                down -= 1
            if direction == 3:
                for i in range(down, up - 1, -1):
                    cnt += 1
                    res[i][left] = cnt
                left += 1
            if cnt == n * n:
                return res
            direction = (direction + 1) % 4
        return res
