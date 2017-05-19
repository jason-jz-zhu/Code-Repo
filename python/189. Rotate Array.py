class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return

        l = len(nums)
        k = k % len(nums)
        self.reverse(nums, 0, l -1 - k)
        self.reverse(nums, l - k, l - 1)
        self.reverse(nums, 0, l - 1)

    def reverse(self, nums, start , end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
