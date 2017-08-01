class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        Solution.res = []
        self.dfs(k, n, 1, [])
        return Solution.res

    def dfs(self, k, n, num, partition):
        if n == 0 and len(partition) == k:
            Solution.res.append(partition)
        if n < 0:
            return
        for i in xrange(num, 10):
            self.dfs(k, n - i, i + 1, partition + [i])
