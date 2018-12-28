class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# binary search
# 特别注意的是list数组的值可能不是一个真实的LIS
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        dp = [float('inf')] * len(nums)
        dp[0] = nums[0]
        size = 0
        for i in range(1, len(nums)):
            index = self.binary_search(dp, nums[i])
            dp[index] = nums[i]
            if index > size:
                size = index
        return size + 1


    def binary_search(self, dp, num):
        start, end = 0, len(dp) - 1
        while start + 1 < end:
            mid = (end - start) / 2 + start
            if dp[mid] < num:
                start = mid
            else:
                end = mid
        if dp[start] >= num:
            return start
        return end
