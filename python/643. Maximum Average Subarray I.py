class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if nums is None or len(nums) < k:
            return -sys.maxint

        s = sum(nums[: k])
        res = s
        end = k
        while end < len(nums):
            s += nums[end] - nums[end - k]
            res = max(res, s)
            end += 1
        return res / 1.0 / k
