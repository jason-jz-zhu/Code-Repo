class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None:
            return False
        if t is None:
            return False
        size_s, size_t = len(s), len(t)

        for i in range(min(size_s, size_t)):
            if s[i] != t[i]:
                if size_s == size_t:
                    return s[i+1:] == t[i+1:]
                elif size_s > size_t:
                    return s[i+1:] == t[i:]
                else:
                    return s[i:] == t[i+1:]

        return abs(size_s - size_t) == 1
                
