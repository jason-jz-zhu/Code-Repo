class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ''
        s_list = list(s)
        start, end = 0, len(s) - 1
        while start < end:
            s_list[start], s_list[end] = s_list[end], s_list[start]
            start += 1
            end -= 1
        return ''.join(s_list)
            
