# DP
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)
            res = max(res, dp[i])
        return res

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)

# DC
# O(nlg(n))
# https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def maxCrossingSum(arr, l, m, h):
            # left side
            s = 0
            left_sum = -float('inf') - 1
            for i in range(m, l - 1, -1):
                s += arr[i]
                if s > left_sum:
                    left_sum = s
            # right side
            s = 0
            right_sum = -float('inf') - 1
            for i in range(m + 1, h + 1):
                s += arr[i]
                if s > right_sum:
                    right_sum = s
            return left_sum + right_sum

        def maxSubArraySum(arr, l, h):
            if l == h:
                return arr[l]

            m = (l + h) // 2

            return max(maxSubArraySum(arr, l, m),
                      maxSubArraySum(arr, m + 1, h),
                      maxCrossingSum(arr, l, m, h))

        return maxSubArraySum(nums, 0, len(nums) - 1)
