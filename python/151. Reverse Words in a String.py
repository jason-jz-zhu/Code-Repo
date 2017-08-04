class Solution(object):
    def reverseWords(self, s):
        return ' '.join(reversed(s.strip().split()))

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return None

        return ' '.join(s.split()[::-1])
