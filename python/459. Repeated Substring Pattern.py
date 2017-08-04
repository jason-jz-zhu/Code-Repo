class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return 0
        l = len(s)
        for i in xrange(1, l / 2 + 1):
            if l % i:
                continue
            if s[: i] * (l / i) == s:
                return True
        return False
