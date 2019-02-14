class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
