class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False

        s_map, t_map = dict(), dict()

        for x in xrange(len(s)):
            if s[x] not in s_map:
                s_map[s[x]] = t[x]
            if t[x] not in t_map:
                t_map[t[x]] = s[x]
            if s_map[s[x]] != t[x] or t_map[t[x]] != s[x]:
                return False
        return True
