class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s is None or t is None or len(t) == 0:
            return ''
        if len(s) == 0 and len(t) == 1:
            return t

        counter = collections.Counter(s)
        for tt in t:
            if counter[tt] == 0:
                return tt
            else:
                counter[tt] -= 1
                

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s is None or t is None or len(t) == 0:
            return ''
        if len(s) == 0 and len(t) == 1:
            return t

        res = 0
        for e in s + t:
            res ^= ord(e)
        return chr(res)


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
