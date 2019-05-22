class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 0:
            return False
        max_reach = 0
        for i in range(len(nums)):
            if max_reach < i:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True



# dp
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums is None or len(nums) == 0:
            return False
        m = len(nums)
        dp = [False for _ in range(m)]
        dp[0] = True

        for j in range(1, m):
            for i in range(j):
                if dp[i] and nums[i] + i >= j:
                    dp[j] = True
                    break
        return dp[-1]
