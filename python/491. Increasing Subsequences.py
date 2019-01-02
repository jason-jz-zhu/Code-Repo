class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        if len(path) > 1:
            res.append(path)
        visited = set()
        for i in range(index, len(nums)):
            if path and path[-1] > nums[i]:
                continue
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            self.dfs(nums, i + 1, path + [nums[i]], res)
            



class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        return [x
                for i in xrange(2, len(nums) + 1)
                for x in set(itertools.combinations(nums, i))
                if all(a <= b for a, b in zip(x, x[1:]))]
