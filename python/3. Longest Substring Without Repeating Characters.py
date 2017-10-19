class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        hashset = set()
        start = end = 0
        res = -1
        while end < len(s):
            if s[end] not in hashset:
                hashset.add(s[end])
                end += 1
                res = max(res, end - start)
            else:
                hashset.remove(s[start])
                start += 1

        return 0 if res == -1 else res




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
