# not accept and dp
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False

        dp = [False] * len(nums)
        dp[0] = True
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                if dp[j] and nums[j] + j >= i:
                    dp[i] = True
                    break
        return dp[len(nums) - 1]

# accept
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False

        m = 0

        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True
