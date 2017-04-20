class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []
        n = len(nums)
        dp = [1] * n
        father = [-1] * n

        nums.sort()
        m, index = 0, -1

        for i in xrange(n):
            for j in xrange(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        father[i] = j
            if dp[i] >= m:
                m = dp[i]
                index = i

        res = []
        for _ in xrange(m):
            res.append(nums[index])
            index = father[index]

        return res
