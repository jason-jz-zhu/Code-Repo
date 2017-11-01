class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        if len(s) == 0:
            return True

        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return self.isPalindrome(s, start, end - 1) or self.isPalindrome(s, start + 1, end)
            start += 1
            end -= 1
        return True

    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
