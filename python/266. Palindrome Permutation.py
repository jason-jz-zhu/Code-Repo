class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import collections
        return sum(v % 2 for v in collections.Counter(s).values()) <  2
        # return sum(v & 1 for v in collections.Counter(s).values()) <  2
