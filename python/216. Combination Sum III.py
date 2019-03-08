class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []
        self.dfs(k, n, 1, [], res)
        return res

    def dfs(self, k, n, index, path, res):
        if len(path) == k and n == 0:
            res.append(path)
            return
        if len(path) > k or n < 0:
            return
        for i in range(index, 10):
            self.dfs(k, n - i, i + 1, path + [i], res)
