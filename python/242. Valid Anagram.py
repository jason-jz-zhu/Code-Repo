class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False

        counter = collections.Counter(s)

        for c in t:
            if c not in counter:
                return False
            counter[c] -= 1
            if counter[c] == 0:
                del counter[c]
        return len(counter) == 0

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or t is None:
            return False
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
