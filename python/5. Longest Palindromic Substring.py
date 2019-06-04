class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ''

        res = ''
        for i in range(len(s)):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]

# dp from right to left
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) == 0:
            return ''
        m = len(s)
        left = right = 0
        longest = 1
        dp = [[False for _ in range(m)] for _ in range(m)]
        for i in range(m):
            dp[i][i] = True

        for i in range(m - 1, -1, -1):
            for j in range(i + 1, m):

                dp[i][j] = (s[i] == s[j]) and (i + 1 == j or dp[i + 1][j - 1])
                if dp[i][j] and longest < j - i + 1:
                    left = i
                    right = j
                    longest = j - i + 1
        return s[left: right + 1]

# dp length from 1 to m
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s is None or len(s) == 0:
            return ''
        m = len(s)
        left = right = 0
        longest = 1
        dp = [[False for _ in range(m)] for _ in range(m)]
        for i in range(m):
            dp[i][i] = True

        for i in range(m - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            if dp[i][i + 1]:
                left, right = i, i + 1
                longest = 2

        for length in range(3, m + 1):
            for i in range(m - length + 1):
                j = i + length - 1
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                if dp[i][j] and longest < j - i + 1:
                    left = i
                    right = j
                    longest = j - i + 1
        return s[left: right + 1]
