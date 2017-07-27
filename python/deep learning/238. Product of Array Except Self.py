# Time O(n) - space O(n)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums

        size = len(nums)
        left = [1] * len(nums)
        res = [1] * len(nums)
        # scan left to right to get all left product
        for i in xrange(1, size):
            left[i] = left[i - 1] * nums[i - 1]
        # scan right to left to get all right product
        for j in xrange(size-2, -1, -1):
            res[j] = res[j + 1] * nums[j + 1]
        # mutil them together
        for i in xrange(size):
            res[i] = res[i] * left[i]

        return res

# Time O(n) - space O(1)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums

        size = len(nums)
        res = [1] * len(nums)
        # scan left to right to get all left product
        for i in xrange(1, size):
            res[i] = res[i - 1] * nums[i - 1]
        right = 1
        # scan right to left
        for j in xrange(size-1, -1, -1):
            res[j] *= right
            right *= nums[j]

        return res
