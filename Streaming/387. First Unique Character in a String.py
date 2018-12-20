class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return -1
        hashmap = collections.Counter(s)
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1
            
