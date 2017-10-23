# using recursively and dfs to search
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            if i != index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)

# using iteratively
class Solution(object):
    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        for i in xrange(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in xrange(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
        return res
