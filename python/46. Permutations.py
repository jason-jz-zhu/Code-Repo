class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) == 0:
            return []
        track = []
        self.res = []
        used = [False] * len(nums)
        self.backtrack(nums, track, used)
        return self.res

    def backtrack(self, nums, track, used):
        if len(track) == len(nums):
            self.res.append(track.copy())
            return
        
        for i in range(len(nums)):
            if used[i]:
                continue
            track.append(nums[i])
            used[i] = True
            self.backtrack(nums, track, used)
            used[i] = False
            track.pop()


# -------------2-25---------


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
