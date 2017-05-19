class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None

        sort = sorted(nums)

        if sort == nums:
            return 0
        start, end = 0, 0
        for i in xrange(len(nums)):
            if sort[i] != nums[i]:
                start = i
                break
        for j in reversed(xrange(len(nums))):
            if sort[j] != nums[j]:
                end = j
                break
        return end - start + 1s

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None

        is_same = [x == y for x, y in zip(nums, sorted(nums))]

        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)
