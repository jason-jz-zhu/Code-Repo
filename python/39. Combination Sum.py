class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Solution.res = []
        if candidates is None or len(candidates) == 0:
            return Solution.res
        candidates.sort()
        partition = []
        self.dfs(candidates, target, 0, partition)
        return Solution.res

    def dfs(self, candidates, target, start_index, partition):
        if target == 0:
            Solution.res.append(partition)
            return
        if target < 0:
            return
        for i in xrange(start_index, len(candidates)):
            self.dfs(candidates, target - candidates[i], i, partition + [candidates[i]])
