class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) <= 1:
            return None
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                temp = nums[left]
                nums[left] = nums[i]
                nums[i] = temp
                left += 1
                i += 1
            elif nums[i] == 2:
                temp = nums[right]
                nums[right] = nums[i]
                nums[i] = temp
                right -= 1
            else:
                i += 1
        
