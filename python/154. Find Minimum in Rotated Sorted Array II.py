class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (end - start) / 2 + start
            if nums[mid] == nums[end]:
                end -= 1
            elif nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])
