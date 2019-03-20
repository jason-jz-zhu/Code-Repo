class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        return self.dfs(s, 0, {}, set(wordDict))

    def dfs(self, s, start, memo, wordDict):
        if start == len(s):
            return True
        if start in memo:
            return memo[start]

        for i in range(start, len(s)):
            sub_str = s[start: i + 1]
            if sub_str not in wordDict:
                continue
            if self.dfs(s, i + 1, memo, wordDict):
                memo[start] = True
                return True
        memo[start] = False
        return False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = dict()
        return self.helper(s, wordSet, memo)

    def helper(self, s: str, wordSet: set, memo: dict) -> bool:
        if s in memo:
            return memo[s]

        if s in wordSet:
            memo[s] = True
            return True

        for i in range(1, len(s)):
            remain = s[i:]
            if remain in wordSet and self.helper(s[0:i], wordSet, memo):
                memo[s] = True
                return True
        memo[s] = False
        return False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = [False] * len(s)
        q = collections.deque([0])
        while q:
            start = q.popleft()
            if visited[start]:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start: end] in wordDict:
                    q.append(end)
                    if end == len(s):
                        return True
            visited[start] = True
        return False

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
