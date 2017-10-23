class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0:
            return []
        res = []
        visited = [False] * len(nums)
        self.dfs(sorted(nums), visited, [], res)
        return res

    def dfs(self, nums, visited, path, res):
        if len(path) == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            if visited[i] or (i != 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                continue
            visited[i] = True
            self.dfs(nums, visited, path + [nums[i]], res)
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
