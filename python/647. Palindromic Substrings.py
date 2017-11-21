class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0

        Solution.res = 0
        for i in range(len(s)):
            self.helper(s, i, i)
            self.helper(s, i, i + 1)

        return Solution.res

    def helper(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
            Solution.res += 1


class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)
        res = 0
        for center in xrange(2 * L - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < L and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
        return res

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def manacher(s):
            s = '^#' + '#'.join(s) + '#$'
            p = [0] * len(s)
            c = r = 0
            for i in xrange(1, len(s) - 1):
                i_mirror = 2 * c - i
                if r > i:
                    p[i] = min(r - i, p[i_mirror])
                while s[i + 1 + p[i]] == s[i - 1 - p[i]]:
                    p[i] += 1
                if i + p[i] > r:
                    c, r = i, i + p[i]
            return p
        return sum((max_len + 1) / 2 for max_len in manacher(s))
