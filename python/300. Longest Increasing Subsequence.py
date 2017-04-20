# dp
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in xrange(n):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1

        return max(dp)

# binary search
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        list = [sys.maxint] * (len(nums) + 1)
        list[0] = -sys.maxint - 1

        for i in xrange(len(nums)):
            index = self.binary_search(list, nums[i])
            list[index] = nums[i]

        for i in xrange(len(nums), 0, -1):
            if list[i] != sys.maxint:
                return i

        return 0

    def binary_search(self, list, num):
        start, end = 0, len(list) - 1
        while start + 1 < end:
            mid = (end - start) / 2 + start
            if list[mid] < num:
                start = mid
            else:
                end = mid
        if list[start] > num:
            return start
        return end
