class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def getRange(lower, upper):
            if lower == upper:
                return '{}'.format(lower)
            else:
                return '{}->{}'.format(lower, upper)

        if nums is None:
            return []
        if len(nums) == 0:
            return [getRange(lower, upper)]

        res = []
        prev = lower - 1
        size = len(nums)
        for i in range(size + 1):
            curr = upper + 1 if i == size else nums[i]

            if curr - prev >= 2:
                res.append(getRange(prev + 1, curr - 1))

            prev = curr
        return res
