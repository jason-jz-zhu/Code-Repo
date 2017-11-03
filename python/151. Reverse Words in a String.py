class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return s

        return ' '.join(s.split()[::-1])
