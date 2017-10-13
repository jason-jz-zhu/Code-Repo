# Time: O(nlogn) Space: O(n)
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        nums_sort = sorted(nums)
        size = len(nums)
        s, t = (size + 1) / 2, size
        for i in range(size):
            if i % 2 == 0:
                s -= 1
                nums[i] = nums_sort[s]
            else:
                t -= 1
                nums[i] = nums_sort[t]

# Time: O(nlogn) Space: O(1)
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        nums.sort()
        half = (len(nums) + 1) / 2
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
