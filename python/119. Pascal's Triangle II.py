class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex is None or rowIndex < 0:
            return []
        res = [1]
        for _ in xrange(1, rowIndex + 1):
            res = map(lambda x, y: x + y, res + [0], [0] + res)
        return res

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(1, rowIndex + 1):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row
