class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or len(candidates) == 0:
            return []

        res = []
        self.dfs(candidates, 0, [], res, target)
        return res

    def dfs(self, candidates, index, path, res, target):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            self.dfs(candidates, i, path + [candidates[i]], res, target - candidates[i])
