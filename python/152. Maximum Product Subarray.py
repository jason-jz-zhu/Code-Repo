class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        cur_max = cur_min = res = nums[0]

        for num in nums[1:]:
            pre_max = cur_max
            cur_max = max(num, num * pre_max, num * cur_min)
            cur_min = min(num, num * pre_max, num * cur_min)
            res = max(res, cur_max)

        return res
