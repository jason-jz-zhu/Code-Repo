class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1

        return sum(sorted(nums)[::2])


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        sort = sorted(nums)
        for i in xrange(len(sort)):
            if i % 2 == 0:
                res += sort[i]

        return res
