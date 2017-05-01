class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in xrange(0, len(s), 2*k):
            if i+k > len(s):
                s[i:] = reversed(s[i:])
            else:
                s[i: i+k] = reversed(s[i : i+k])
        return ''.join(s)
