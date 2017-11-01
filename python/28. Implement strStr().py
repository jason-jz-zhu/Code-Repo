# becuase we use the python, using haystack[i: lenN+i] is very easy
# to get part of string
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        size_h = len(haystack)
        size_n = len(needle)
        for i in range(size_h - size_n + 1):
            if haystack[i: size_n + i] == needle:
                return i
        return -1

# this method is the normal one using two for loop
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        lenH = len(haystack)
        lenN = len(needle)
        for i in xrange(lenH-lenN+1):
            total = 0
            for j in xrange(lenN):
                if needle[j] != haystack[i + j]:
                    break
                total += 1
            if total == lenN: return i

        return -1
