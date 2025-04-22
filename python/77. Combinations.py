class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        track = []
        self.backtrack(1, n, k, track)
        return self.res

    def backtrack(self, start, n, k, track):
        if len(track) == k:
            self.res.append(track.copy())
            return
        for i in range(start, n + 1):
            track.append(i)
            self.backtrack(i + 1, n, k, track)
            track.pop()

# -----------2025----------

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(n, k, 1, [], res)
        return res

    def dfs(self, n, k, index, path, res):
        if len(path) == k:
            res.append(path)
            return
        for i in range(index, n + 1):
            self.dfs(n, k, i + 1, path + [i], res)
        
