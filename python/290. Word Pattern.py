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
        str_list = str.split(' ')
        if len(pattern) != len(str_list):
            return False
        p_map, s_map = dict(), dict()
        for p, s in zip(pattern, str_list):
            if p not in p_map:
                p_map[p] = s
            if s not in s_map:
                s_map[s] = p
            if p_map[p] != s or s_map[s] != p:
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
