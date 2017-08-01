class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        pre = lower - 1

        for i in xrange(len(nums) + 1):
            cur = upper + 1 if i == len(nums) else nums[i]

            if cur - pre >= 2:
                res.append(self.getRange(pre + 1, cur - 1))

            pre = cur
        return res

    def getRange(self, lower, upper):
        if lower == upper:
            return '{}'.format(lower)
        else:
            return '{}->{}'.format(lower, upper)
