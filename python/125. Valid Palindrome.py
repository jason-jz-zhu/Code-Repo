class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False

        if len(s) == 0:
            return True

        head, tail = 0, len(s) - 1
        while head < tail:
            while head < tail and not s[head].isalpha() and not s[head].isdigit():
                head += 1
            while head < tail and not s[tail].isalpha() and not s[tail].isdigit():
                tail -= 1
            if s[head].lower() != s[tail].lower():
                return False
            head += 1
            tail -= 1
        return True
