class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        f = [0 for _ in range(len(nums))]
        f[0] = nums[0]
        f[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            f[i] = max(f[i - 1], f[i - 2] + nums[i])
        return f[-1]
