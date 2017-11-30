class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None:
            return False
        if t is None:
            return False
        if len(t) != len(s):
            return False

        s_hashmap, t_hashmap = {}, {}

        for ss, tt in zip(s, t):
            if ss not in s_hashmap:
                s_hashmap[ss] = tt
            if tt not in t_hashmap:
                t_hashmap[tt] = ss
            if s_hashmap[ss] != tt or t_hashmap[tt] != ss:
                return False

        return True
