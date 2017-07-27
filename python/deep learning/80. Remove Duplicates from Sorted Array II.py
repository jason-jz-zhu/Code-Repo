class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0
        if len(nums) < 2:
            return len(nums)

        end = 0

        for i in xrange(len(nums)):
            if end < 2 or nums[i] != nums[end - 1] or nums[i] != nums[end - 2]:
                nums[end] = nums[i]
                end += 1
        return end
