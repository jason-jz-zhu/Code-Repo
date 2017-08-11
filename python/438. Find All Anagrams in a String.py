class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        import collections
        res = []
        pCounter = collections.Counter(p)
        sCounter = collections.Counter(s[: len(p) - 1])
        for i in xrange(len(p) - 1, len(s)):
            sCounter[s[i]] += 1
            if sCounter == pCounter:
                res.append(i - len(p) + 1)
            sCounter[s[i - len(p) + 1]] -= 1
            if sCounter[s[i - len(p) + 1]] == 0:
                del sCounter[s[i - len(p) + 1]]
        return res



class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if s is None:
            return []

        res = []
        # container
        hash = [0 for x in xrange(26)]
        s_length, p_length = len(s), len(p)
        start = end = 0
        matched = 0
        for item in p:
            hash[ord(item) - ord('a')] += 1
        # main loop
        while end < s_length:
            if hash[ord(s[end]) - ord('a')] >= 1:
                matched += 1
            hash[ord(s[end]) - ord('a')] -= 1
            end += 1
            if matched == p_length:
                res.append(start)
            # window exceed the size
            # need to move start
            if end - start == p_length:
                # because end has gone through the string,
                # >= 0 means this item is in p
                if hash[ord(s[start]) - ord('a')] >= 0:
                    matched -= 1
                hash[ord(s[start]) - ord('a')] += 1
                start += 1
        return res
