class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if target <= nums[start]:
            return start
        elif target <= nums[end]:
            return end
        else:
            return end + 1
