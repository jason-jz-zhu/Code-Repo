# with memoization
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashmap = {}
        return self.helper(s, hashmap)

    def helper(self, s, hashmap):
        if s not in hashmap:
            hashmap[s] = any(s[i:i+2] == '++' and not self.canWin(s[:i] + '-' + s[i+2:]) for i in range(len(s)))
        return hashmap[s]

# without memoization
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s) - 1):
            if s[i: i + 2] == '++' and not self.canWin(s[: i] + '--' + s[i + 2:]):
                return True
        return False
