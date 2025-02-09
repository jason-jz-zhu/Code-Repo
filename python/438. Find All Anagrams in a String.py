class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = {}
        need = {}
        for c in p:
            need[c] = need.get(c, 0) + 1
        left = right = 0
        valid = 0
        res = []

        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res



class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        import collections
        res = []
        p_counter = collections.Counter(p)
        s_counter = collections.Counter(s[: len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            s_counter[s[i]] += 1
            if s_counter == p_counter:
                res.append(i - len(p) + 1)
            s_counter[s[i - len(p) + 1]] -= 1
            if s_counter[s[i - len(p) + 1]] == 0:
                del s_counter[s[i - len(p) + 1]]
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
