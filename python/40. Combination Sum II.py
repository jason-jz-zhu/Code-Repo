class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or len(candidates) == 0:
            return []

        res = []
        candidates.sort()
        self.dfs(candidates, 0, [], res, target)
        return res

    def dfs(self, candidates, index, path, res, target):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            if i != index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, i + 1, path + [candidates[i]], res, target - candidates[i])
