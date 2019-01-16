# not accept and dp
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False
        f = [False for _ in range(len(nums))]
        f[0] = True
        for i in range(1, len(nums)):
            for j in range(i):
                if f[j] and nums[j] + j >= i:
                    f[i] = True
                    break
        return f[-1]

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
