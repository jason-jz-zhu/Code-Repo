class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        def helper(M, i, j):
            directions = [[-1, -1], [0, -1], [1, -1], \
                          [-1,  0], [0,  0], [1,  0], \
                          [-1,  1], [0,  1], [1,  1]]
            total, cnt = 0, 0
            for d in directions:
                ii, jj = i + d[0], j + d[1]
                if 0 <= ii < len(M) and 0 <= jj < len(M[0]):
                    total += M[ii][jj]
                    cnt += 1
            return int(total / cnt)

        res = [[0 for _ in xrange(len(M[0]))] for _ in xrange(len(M))]
        for i in xrange(len(M)):
            for j in xrange(len(M[0])):
                res[i][j] = helper(M, i, j)
        return res
