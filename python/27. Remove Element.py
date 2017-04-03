class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        end = 0
        for i in xrange(len(nums)):
            if nums[i] != val:
                nums[end] = nums[i]
                end += 1
        return end
