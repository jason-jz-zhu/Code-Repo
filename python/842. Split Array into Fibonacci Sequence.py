class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        if not S or len(S) == 0:
            return []

        res = []
        self.max_int = 2 ** 31 - 1
        self.dfs(S, 0, [], res)
        return res[0] if res else []

    def dfs(self, S, start, path, res):
        if start == len(S) and len(path) >= 3:
            res.append(path)
            return True

        for i in range(start, len(S)):
            substr = S[start: i + 1]
            if len(substr) > 1 and substr[0] == '0':
                break
            num = int(substr)
            if num > self.max_int:
                break
            if len(path) >= 2:
                s = path[-1] + path[-2]
                if num > s:
                    break
                elif num < s:
                    continue
            if self.dfs(S, i + 1, path + [num], res):
                return True
        return False
