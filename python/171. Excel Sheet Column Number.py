class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for ss in s:
            res = res * 26 + ord(ss) - ord('A') + 1
        return res
