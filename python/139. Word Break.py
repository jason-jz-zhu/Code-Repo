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

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s is None or len(s) == 0:
            return False
        if wordDict is None or len(wordDict) == 0:
            return False
        m = len(s)
        dp = [False for _ in range(m + 1)]
        dp[0] = True
        for j in range(1, m + 1):
            for i in range(j):
                if dp[i] and s[i: j] in set(wordDict):
                    dp[j] = True
                    break
        return dp[-1]
