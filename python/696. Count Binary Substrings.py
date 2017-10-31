class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, prev, curr = 0, 0, 1
        for i in xrange(1, len(s)):
            if s[i-1] != s[i]:
                res += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1
        res += min(prev, curr)
        return res
