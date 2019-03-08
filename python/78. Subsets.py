class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) == 0:
            return []

        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

# using iteratively
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        for curr in nums:
            tmp = [prev + [curr] for prev in res]
            res += tmp
        return res

            
