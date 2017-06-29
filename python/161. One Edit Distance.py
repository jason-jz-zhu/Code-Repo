class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls, lt = len(s), len(t)
        for i in xrange(min(ls, lt)):
            if s[i] != t[i]:
                if ls == lt:
                    return s[i+1:] == t[i+1:]
                elif ls > lt:
                    return s[i+1:] == t[i:]
                else:
                    return s[i:] == t[i+1:]
        return abs(len(s) - len(t)) == 1
