class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = map(str, range(1, n + 1))
        while len(res) / 2:
            res = ['({},{})'.format(res[i], res[-i - 1]) for i in range(len(res) / 2)]
        return res[0]
