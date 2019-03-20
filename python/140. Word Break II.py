class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        can_break = [True] * len(s)
        self.dfs(s, 0, set(wordDict), [], can_break, res)
        return res

    def dfs(self, s, start, wordDict, path, can_break, res):
        if start == len(s):
            res.append(' '.join(path))
            return

        if not can_break[start]:
            return

        for i in range(start, len(s)):
            sub_str = s[start: i + 1]
            if sub_str not in wordDict:
                continue

            before_change = len(res)
            self.dfs(s, i + 1, wordDict, path + [sub_str], can_break, res)
            if len(res) == before_change:
                can_break[i + 1] = False

        
