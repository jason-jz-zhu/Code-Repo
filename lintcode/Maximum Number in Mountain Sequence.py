class Solution:
    # @param {int[]} nums a mountain sequence
    # which increase firstly and then decrease
    # @return {int} then mountain top
    def mountainSequence(self, nums):
        # Write your code here
        if nums is None or len(nums) == 0:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid1 = start + (end - start) / 2
            mid2 = end - (end - mid1) / 2
            if nums[mid1] < nums[mid2]:
                start = mid1 + 1
            elif nums[mid1] > nums[mid2]:
                end = mid2 - 1
            else:
                start = mid1
                end = mid2
        return max(nums[start], nums[end])
