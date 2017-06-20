class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)

        res = 0

        for key in counter:
            if key + 1 in counter:
                res = max(res, counter[key] + counter[key + 1])
        return res
