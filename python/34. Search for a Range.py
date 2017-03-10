class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        if nums is None or len(nums) == 0:
            return [-1, -1]
        # find the first one
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            res.append(start)
        elif nums[end] == target:
            res.append(end)
        else:
            res.append(-1)
        # find the last one
        end = len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        if nums[end] == target:
            res.append(end)
        elif nums[start] == target:
            res.append(start)
        else:
            res.append(-1)
        return res
