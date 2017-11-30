class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if pattern is None or len(pattern) == 0:
            return False
        if str is None or len(str) == 0:
            return False
        str_list = str.split()
        if len(pattern) != len(str_list):
            return False
        p_hashmap, s_hashmap = {}, {}
        for p, s in zip(pattern, str_list):
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
