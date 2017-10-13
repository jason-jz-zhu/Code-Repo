class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i in xrange(len(nums)) if nums[i] > 0]

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        while i <= len(nums) - 1:
            if nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        res = []
        for i in xrange(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res
