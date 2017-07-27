class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return False
        if wordDict is None or len(wordDict) == 0:
            return False

        map = collections.Counter(wordDict)
        dp = [False for i in xrange(len(s) + 1)]
        dp[0] = True
        for i in xrange(1, len(s) + 1):
            for j in xrange(i):
                if dp[j] and s[j: i] in map:
                    dp[i] = True
        return dp[len(s)]
        
