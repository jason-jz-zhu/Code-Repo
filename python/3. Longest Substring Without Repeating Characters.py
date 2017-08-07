class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = res = 0
        hashmap = {}
        for i in xrange(len(s)):
            if s[i] in hashmap and left <= hashmap[s[i]]:
                left = hashmap[s[i]] + 1
            hashmap[s[i]] = i
            res = max(res, i - left + 1)
        return res
