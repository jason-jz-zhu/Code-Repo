class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif mid % 2 == 1 and nums[mid] == nums[mid - 1]:
                start = mid
            elif mid % 2 == 0 and nums[mid] == nums[mid + 1]:
                start = mid
            else:
                end = mid
        if start == 0 and nums[start] != nums[start + 1]:
            return nums[start]
        if end == len(nums) - 1 and nums[end] != nums[end - 1]:
            return nums[end]

        return nums[end] if nums[end] != nums[end - 1] and nums[end] != nums[end + 1] else nums[start]
