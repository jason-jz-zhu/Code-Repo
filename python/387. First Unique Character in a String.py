class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return -1

        freq = {}
        for e in s:
            freq[e] = freq.get(e, 0) + 1
        for i in xrange(len(s)):
            if freq.get(s[i]) == 1:
                return i
        return -1
