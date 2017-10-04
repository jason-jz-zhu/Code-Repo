class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1
        res = 0
        for i in range(len(nums)):
            res ^= (i + 1) ^ nums[i]
        return res

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1
        l = len(nums)
        sum1 = l * (l + 1) / 2
        sum2 = reduce(lambda x, y: x + y, nums)
        return sum1 - sum2
