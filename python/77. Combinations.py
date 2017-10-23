class Solution:
    from itertools import combinations
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(k, n, 1, [], res)
        return res

    def dfs(self, k, n, index, path, res):
        if len(path) == k:
            res.append(path)
            return
        for i in range(index, n + 1):
            self.dfs(k, n, i + 1, path + [i], res)
