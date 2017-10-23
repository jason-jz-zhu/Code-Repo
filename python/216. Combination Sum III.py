class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(k, n, 1, [], res)
        return res

    def dfs(self, k, n, index, path, res):
        if n == 0 and len(path) == k:
            res.append(path)
            return
        if n < 0:
            return
        for i in range(index, 10):
            self.dfs(k, n - i, i + 1, path + [i], res)
