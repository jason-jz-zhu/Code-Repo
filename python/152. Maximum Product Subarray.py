class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        global_max = prev_max = prev_min = nums[0]
        for num in nums[1:]:
            if num > 0:
                curr_max = max(num, prev_max * num)
                curr_min = min(num, prev_min * num)
            else:
                curr_max = max(num, prev_min * num)
                curr_min = min(num, prev_max * num)
            global_max = max(global_max, curr_max)
            prev_max, prev_min = curr_max, curr_min
        return global_max
