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
        
