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
