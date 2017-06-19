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
        for x in range(len(s)):
            source, target = s_map.get(t[x]), t_map.get(s[x])
            if source is None and target is None:
                s_map[t[x]], t_map[s[x]] = s[x], t[x]
            elif target != t[x] or source != s[x]:
                return False
        return True
