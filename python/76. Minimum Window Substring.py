class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        hashmap = collections.Counter(t)
        start = end = 0
        cnt = len(t)
        res = '#'
        while end < len(s):
            if hashmap[s[end]] > 0:
                cnt -= 1
            hashmap[s[end]] -= 1
            end += 1
            while start < end and cnt == 0:
                if res == '#' or len(res) > end - start:
                    res = s[start: end]
                hashmap[s[start]] += 1
                if hashmap[s[start]] > 0:
                    cnt += 1
                start += 1
        return '' if res == '#' else res 
