class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(len(nums)):
            res ^= (i + 1) ^ nums[i]
        return res

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum1 = n * (n + 1) / 2
        sum2 = reduce(lambda x, y: x + y, nums)
        return sum1 - sum2
