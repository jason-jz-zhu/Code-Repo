class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        res = 0
        has_odd = False
        counter = collections.Counter(s)

        for v in counter.values():
            if v % 2 == 0:
                res += v
            else:
                has_odd = True
                res += v - 1

        return res + 1 if has_odd else res
