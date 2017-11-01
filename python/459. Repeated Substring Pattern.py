class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return 0
        size = len(s)
        for i in range(1, size / 2 + 1):
            if size % i != 0:
                continue
            if s[: i] * (size / i) == s:
                return True
        return False
