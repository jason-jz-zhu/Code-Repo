class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return False
        a = 0
        for i in xrange(len(s)):
            if s[i] == 'A':
                a += 1
                if a == 2:
                    return False
            if i < len(s) - 2 and s[i] == s[i + 1] == s[i + 2] == 'L':
                return False
        return True
