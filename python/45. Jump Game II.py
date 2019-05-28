class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        near = far = 0
        for i in range(len(nums)):
            if i > near:
                res += 1
                near = far
            far = max(far, nums[i] + i)
        return res


class Solution:
    def jump(self, nums: List[int]) -> int:
        m = len(nums)
        dp = [float('inf')] * m
        dp[0] = 0
        for i in range(1, m):
            for j in range(i):
                if nums[j] + j >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
