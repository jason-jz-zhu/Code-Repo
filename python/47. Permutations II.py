# using recursively and dfs to search
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if nums is None:
            return res
        visited = [False for i in xrange(len(nums))]
        self.dfs(sorted(nums), [], res, visited)
        return res

    def dfs(self, nums, path, res, visited):
        if len(path) == len(nums):
            res.append(path)
        for i in xrange(len(nums)):
            if visited[i] or (i != 0 and nums[i] == nums[i-1] and not visited[i-1]):
                continue
            visited[i] = True
            self.dfs(nums, path+[nums[i]], res, visited)
            visited[i] = False

# using iteratively and reduce function
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return reduce(lambda P, n: [p[:i] + [n] + p[i:] for p in P for i in xrange((p + [n]).index(n) + 1)],
                            nums, [[]])
