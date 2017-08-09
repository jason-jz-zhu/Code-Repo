class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        dp = [[0 for j in xrange(len(word2) + 1)] for i in xrange(len(word1) + 1)]
        for i in xrange(len(word1) + 1):
            for j in xrange(len(word2) + 1):
                if i == 0 or j == 0:
                    continue
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return len(word1) + len(word2) - 2 * dp[len(word1)][len(word2)]
    
# TIme Limit Exceeded
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        def lcs(w1, w2, m, n, memo):
            if m == 0 or n == 0:
                return 0
            if memo[m][n] > 0:
                return memo[m][n]
            if w1[m - 1] == w2[n - 1]:
                memo[m][n] = 1 + lcs(w1, w2, m - 1, n - 1, memo)
            else:
                memo[m][n] = max(lcs(w1, w2, m, n - 1, memo), lcs(w1, w2, m - 1, n, memo))
            return memo[m][n]

        memo = [[0 for j in xrange(len(word2) + 1)] for i in xrange(len(word1) + 1)]
        return len(word1) + len(word2) - 2 * lcs(word1, word2, len(word1), len(word2), memo)
