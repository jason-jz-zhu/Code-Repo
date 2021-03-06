class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) < 2:
            return
        first_num = -1
        # 1. from right to left, find the first num which is smaller than before
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                first_num = i
                break
        # 2.
        if first_num == -1:
            nums.reverse()
            return
        # 3. from right to first_num, find the first num which is larger than first_num, and swap them
        for j in range(len(nums) - 1, first_num, -1):
            if nums[j] > nums[first_num]:
                nums[j], nums[first_num] = nums[first_num], nums[j]
                break
        # 4. reverse all nums after first_num
        start, end = first_num + 1, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return
