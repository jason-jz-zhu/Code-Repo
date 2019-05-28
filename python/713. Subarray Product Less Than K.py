class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        m = len(nums)
        left = right = 0
        res = 0
        prod = 1
        while right < m:
            prod *= nums[right]
            while left < right and prod >= k:
                prod /= nums[left]
                left += 1
            if prod < k:
                res += right - left + 1
            right += 1
        return res
