class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] == target:
                return mid
            if nums[start] < nums[mid]:
                if nums[mid] >= target and nums[start] <= target:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] <= target and nums[end] >= target:
                    start = mid
                else:
                    end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
