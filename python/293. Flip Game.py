class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in xrange(1, len(s)):
            if s[i - 1: i + 1] == '++':
                res.append(s[: i - 1] + '--' + s[i + 1: ])
        return res

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [s[: i - 1] + '--' + s[i + 1: ] for i in xrange(1, len(s)) if s[i - 1: i + 1] == '++']
