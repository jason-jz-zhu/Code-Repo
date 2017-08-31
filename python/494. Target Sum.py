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

# dfs  Time Limit Exceeded
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        size = len(nums)
        rSum = [0] * size
        rSum[-1] = nums[-1]
        for i in xrange(size-2, -1, -1):
            rSum[i] = rSum[i+1] + nums[i]
        Solution.res = 0
        self.dfs(nums, S, 0, 0, rSum)
        return Solution.res

    def dfs(self, nums, S, idx, curSum, rSum):
        if idx == len(nums):
            if curSum == S:
                Solution.res += 1
        elif abs(S - curSum) <= rSum[idx]:
            self.dfs(nums, S, idx + 1, curSum + nums[idx], rSum)
            self.dfs(nums, S, idx + 1, curSum - nums[idx], rSum)


# dfs  Time Limit Exceeded
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
        self.dfsHelper(nums, S, 0, 0)
        return self.res

    def dfsHelper(self, nums, S, i, currSum):
        if i == len(nums):
            if currSum == S:
                self.res += 1
        else:
            self.dfsHelper(nums, S, i + 1, currSum + nums[i])
            self.dfsHelper(nums, S, i + 1, currSum - nums[i])
