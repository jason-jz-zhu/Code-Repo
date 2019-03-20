class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        res = []
        self.max_int = 2 ** 31 - 1
        self.dfs(S, 0, [], res)
        return res

    def dfs(self, S, start, path, res):
        if start == len(S) and len(path) >= 3:
            res.append(path)
            return True

        for i in range(start, len(S)):
            sub_str = S[start: i + 1]
            if len(sub_str) > 1 and sub_str[0] == '0':
                break
            d = int(sub_str)
            if d > self.max_int:
                break
            if len(path) >= 2:
                s = sum(path[-2:])
                if d > s:
                    break
                elif d < s:
                    continue
            if self.dfs(S, i + 1, path + [d], res):
                return True
        return False
