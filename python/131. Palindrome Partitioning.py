class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s or len(s) == 0:
            return []

        res = []
        self.dfs(s, 0, [], res)
        return res

    def dfs(self, s, start, path, res):
        if start == len(s):
            res.append(path)
            return

        for i in range(start, len(s)):
            substring = s[start: i + 1]
            if not self.is_pal(substring):
                continue
            self.dfs(s, i + 1, path + [substring], res)

    def is_pal(self, s):
        return s == s[::-1]
