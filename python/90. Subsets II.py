class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, path + [nums[i]], res)

# using iteratively
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        tmp = []
        for i, curr in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                tmp = [prev + [curr] for prev in tmp]
            else:
                tmp = [prev + [curr] for prev in res]
            res += tmp
        return res
