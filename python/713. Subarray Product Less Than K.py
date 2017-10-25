class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        start = end = 0
        size = len(nums)
        product = 1
        res = 0
        while end < size:
            product *= nums[end]

            while start < end and product >= k:
                product /= nums[start]
                start += 1

            if product < k:
                res += end - start + 1
            end += 1
        return res
                
