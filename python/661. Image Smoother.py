class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def helper(M, i, j):
            dx = [-1, -1, -1, 0, 0, 1, 1, 1, 0]
            dy = [-1, 0, 1, 1, -1, -1, 0, 1, 0]
            s = cnt = 0
            for k in range(9):
                x, y = i + dx[k], j + dy[k]
                if x >= 0 and y >= 0 and x < len(M) and y < len(M[0]):
                    s += M[x][y]
                    cnt += 1
            return int(s / cnt)

        if M is None or len(M) == 0 or len(M[0]) == 0:
            return []

        res = [[0 for _ in range(len(M[0]))] for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                res[i][j] = helper(M, i, j)

        return res
