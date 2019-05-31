class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        m = len(nums)
        dp = [0] * m
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, m):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
