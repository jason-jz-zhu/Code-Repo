class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(s):
            return False
        dict = {}
        for c in s:
            dict[c] = dict.get(c, 0) + 1

        for c in t:
            if c not in dict:
                return False
            dict[c] -= 1
            if dict[c] == 0:
                del dict[c]

        return len(dict) == 0
