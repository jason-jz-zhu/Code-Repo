class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (end - start) / 2 + start
            if nums[mid] == target:
                return True
            if nums[mid] < nums[end]:
                if nums[mid] < target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
            elif nums[mid] > nums[end]:
                if nums[start] <= target and target < nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                end -= 1

        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False
