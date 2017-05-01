class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash = {}
        for e in s:
            hash[e] = hash.get(e, 0) + 1
        for e in t:
            if hash.get(e, 0) == 0:
                return e
            else:
                hash[e] -= 1

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        diff = 0
        for i in xrange(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])
        diff += ord(t[-1])
        return chr(diff)

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        code = 0
        for e in s + t:
            code ^= ord(e)
        return chr(code)
