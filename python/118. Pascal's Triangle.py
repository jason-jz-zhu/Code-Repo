class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            row = [x + y for x, y in zip([0] + res[-1], res[-1] + [0])]
            res.append(row)
        return res

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

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        last = self.generate(numRows - 1)
        row = []
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                row.append(1)
            else:
                row.append(last[-1][i - 1] + last[-1][i])
        last.append(row)
        return last
        
