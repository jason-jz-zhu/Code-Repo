class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return

        end = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[end] = nums[i]
                end += 1

        while end < len(nums):
            nums[end] = 0
            end += 1


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return

        last = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[curr], nums[last] = nums[last], nums[curr]
                last += 1
