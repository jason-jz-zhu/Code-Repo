class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = [max(x, x[::-1]) for x in strs]
        res = -sys.maxint
        for i, cur in enumerate(s):
            for start in (cur, cur[::-1]):
                for j in xrange(len(start) + 1):
                    res = max(res, start[j:] + ''.join(s[i + 1:] + s[: i]) + start[: j])
        return res
