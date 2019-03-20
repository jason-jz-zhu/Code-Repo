class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = collections.Counter(s)
        mid = ''.join([k for k, v in counter.items() if v % 2])
        chars = ''.join([k * (v // 2) for k, v in counter.items()])
        if len(mid) >= 2:
            return []

        res = []
        visited = [False] * len(chars)
        self.dfs(chars, mid, visited, '', res)
        return res

    def dfs(self, chars, mid, visited, path, res):
        if len(path) == len(chars):
            tmp = path + mid + path[::-1]
            res.append(tmp)
            return
        for i in range(len(chars)):
            if visited[i] or (i != 0 and not visited[i - 1] and chars[i - 1] == chars[i]):
                continue
            visited[i] = True
            self.dfs(chars, mid, visited, path + chars[i], res)
            visited[i] = False
