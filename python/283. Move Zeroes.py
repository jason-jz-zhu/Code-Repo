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

        start = end = 0

        while end < len(nums):
            if nums[end] != 0:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
            end += 1
