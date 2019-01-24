# dp
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        from collections import defaultdict
        hashmap = {0: 1}
        for num in nums:
            m = defaultdict(int)
            for s, n in hashmap.iteritems():
                m[s + num] += n
                m[s - num] += n
            hashmap = m
        return hashmap[S]


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def findTarget(i, s):
            if (i, s) not in cache:
                r = 0
                if i == len(nums):
                    if s == 0:
                        r = 1
                else:
                    r = findTarget(i+1, s-nums[i]) + findTarget(i+1, s+nums[i])
                cache[(i, s)] = r
            return cache[(i, s)]

        cache = {}
        return findTarget(0, S)


# dfs
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        self.res = 0
        self.dfs(nums, S, 0)
        return self.res

    def dfs(self, nums, S, i):
        if i >= len(nums):
            if S == 0:
                self.res += 1
            return
        self.dfs(nums, S - nums[i], i + 1)
        self.dfs(nums, S + nums[i], i + 1)
