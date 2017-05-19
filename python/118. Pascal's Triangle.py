class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows is None or numRows <= 0:
            return []
        res = []
        for i in xrange(numRows):
            res.append([1] * (i + 1))
            if i > 1:
                for j in xrange(1, i):
                    res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows is None or numRows <= 0:
            return []
        res = [[1]]
        for i in xrange(1, numRows):
            res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]
        return res
