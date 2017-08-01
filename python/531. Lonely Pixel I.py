class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        if picture is None or len(picture) == 0:
            return 0

        m, n = len(picture), len(picture[0])
        row, col = [0] * m, [0] * n
        for i in xrange(m):
            for j in xrange(n):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                if picture[i][j] == 'B':
                    if row[i] == 1 and col[j] == 1:
                        res += 1
        return res
