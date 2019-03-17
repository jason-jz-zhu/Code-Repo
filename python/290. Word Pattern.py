class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern or len(pattern) == 0:
            return False
        if not s or len(s) == 0:
            return False
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False
        p_hashmap, s_hashmap = {}, {}

        mapping = zip(list(pattern), s_list)

        for p, s in mapping:
            if p not in p_hashmap:
                p_hashmap[p] = s
            if s not in s_hashmap:
                s_hashmap[s] = p
            if p_hashmap[p] != s or s_hashmap[s] != p:
                return False
        return True


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s = pattern
        t = str.split()
        return map(s.find, s) == map(t.index, t)
