class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        step, res = 2 * numRows - 2, ''
        for i in xrange(numRows):
            for j in xrange(i, len(s), step):
                res += s[j]
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    res += s[j + step - 2 * i]
        return res
