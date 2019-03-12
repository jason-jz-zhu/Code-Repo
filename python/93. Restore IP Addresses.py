class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s or len(s) == 0:
            return []
        res = []
        self.dfs(s, 0, [], res)
        return res

    def dfs(self, s, start, path, res):
        if len(path) == 4:
            if start == len(s):
                res.append('.'.join(path))
            return

        for i in range(start, start + 3):
            substring = s[start: i + 1]
            if not self.is_valid(substring) and len(s) > i:
                continue
            self.dfs(s, i + 1, path + [substring], res)

    def is_valid(self, s):
        if len(s) == 0 or len(s) > 3:
            return False
        return int(s) <= 255 if s[0] != '0' else len(s) == 1
