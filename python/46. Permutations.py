class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path)
            
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            self.dfs(nums, path + [nums[i]], res)

# using iteratively and reduce function
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return reduce(lambda P, n: [p[:i] + [n] + p[i:] for p in P for i in xrange(len(p)+1)],
                        nums, [[]])
