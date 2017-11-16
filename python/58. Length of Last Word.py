class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        tmp = s.split()
        return len(tmp[-1]) if len(tmp) != 0 else 0
