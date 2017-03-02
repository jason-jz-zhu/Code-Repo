class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None: return -1
        lenH = len(haystack)
        lenN = len(needle)
        for i in xrange(lenH-lenN+1):
            if haystack[i: lenN+i] == needle: return i
            
        return -1