class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Solution.res = []
        if candidates is None or len(candidates) == 0:
            return Solution.res
        partition = []
        candidates.sort()
        self.dfs(candidates, target, 0, partition)
        return Solution.res

    def dfs(self, candidates, target, start_index, partition):
        if target == 0:
            Solution.res.append(partition)
            return
        if target < 0:
            return
        for i in xrange(start_index, len(candidates)):
            if i != start_index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, target - candidates[i], i + 1, partition + [candidates[i]])
