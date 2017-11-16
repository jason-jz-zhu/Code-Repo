class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        hashmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        i = len(s) - 2
        res = hashmap[s[-1]]
        while i >= 0:
            if hashmap[s[i]] < hashmap[s[i + 1]]:
                res -= hashmap[s[i]]
            else:
                res += hashmap[s[i]]
            i -= 1
        return res
