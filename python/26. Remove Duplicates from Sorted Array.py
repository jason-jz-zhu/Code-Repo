class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        end = 0

        for i in xrange(len(nums)):
            if i == 0 or nums[i] != nums[end - 1]:
                nums[end] = nums[i]
                end += 1
        return end
