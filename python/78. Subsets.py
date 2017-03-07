# using recursively and dfs to search
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if nums is None:
            return res
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):

            self.dfs(nums, i+1, path+[nums[i]], res)

# using iteratively
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res += [ [num]+item for item in res]
        return res
