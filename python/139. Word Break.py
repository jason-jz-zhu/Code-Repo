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


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        hashset = set(wordDict)
        visited = [0] * len(s)
        q = collections.deque([0])
        while q:
            start = q.popleft()
            if visited[start] == 0:
                for end in range(start + 1, len(s) + 1):
                    if s[start: end] in hashset:
                        q.append(end)
                        if end == len(s):
                            return True
                visited[start] = 1
        return False
