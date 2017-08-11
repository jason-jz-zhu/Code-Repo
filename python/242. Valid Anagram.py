class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hashmap = collections.Counter(s)
        for c in t:
            if c not in hashmap:
                return False
            hashmap[c] -= 1
            if hashmap[c] == 0:
                del hashmap[c]
        return len(hashmap) == 0
