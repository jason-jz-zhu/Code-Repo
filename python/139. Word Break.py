# dp
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        self.memo = [-1 for _ in range(len(s))]
        return self.dp(s, 0)

    def dp(self, s, i):
        # base case, s[i..] is an empty string
        if i == len(s):
            return True
        if self.memo[i] == 0:
            return False
        if self.memo[i] == 1:
            return True
        
        # Traverse all prefixes of s[i..], check which prefixes exist in wordDict
        for length in range(1, len(s) - i + 1):
            # s[i..len) exists in wordDict
            prefix = s[i: i + length]
            if prefix in self.wordDict:
                sub_problem = self.dp(s, i + length)
                if sub_problem is True:
                    self.memo[i] = 1
                    return True
        
        self.memo[i] = 0
        # All words have been tried, unable to form the entire s
        return False



# add memo
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.res = False
        track = []
        self.memo = set()
        self.backtrack(s, wordDict, 0, track)
        return self.res

    def backtrack(self, s, wordDict, i, track):
        if self.res:
            return
        if i == len(s):
            self.res = True
            return
        suffix = s[i:]
        if suffix in self.memo:
            return
        for word in wordDict:
            length = len(word)
            if i + length > len(s) or s[i: i + length] != word:
                continue
            track.append(word)
            self.backtrack(s, wordDict, i + length, track)
            track.pop()
        
        if not self.res:
            self.memo.add(suffix)

# time limited
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.res = False
        track = []
        self.backtrack(s, wordDict, 0, track)
        return self.res

    def backtrack(self, s, wordDict, i, track):
        if self.res:
            return
        if i == len(s):
            self.res = True
            return

        for word in wordDict:
            length = len(word)
            if i + length > len(s) or s[i: i + length] != word:
                continue
            track.append(word)
            self.backtrack(s, wordDict, i + length, track)
            track.pop()

# --------2025

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
