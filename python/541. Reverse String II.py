class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in xrange(0, len(s), 2*k):
            if i+k > len(s):
                s[i:] = reversed(s[i:])
            else:
                s[i: i+k] = reversed(s[i : i+k])
        return ''.join(s)

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote is None or len(ransomNote) == 0:
            return True
        if magazine is None:
            return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)
