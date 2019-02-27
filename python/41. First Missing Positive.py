class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 1
        m = len(nums)
        if 1 not in nums:
            return 1
        if m == 1:
            return 2

        for i in range(m):
            if nums[i] <= 0 or nums[i] > m:
                nums[i] = 1

        for num in nums:
            a = abs(num)
            if a == m:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])

        for i in range(1, m):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return m
        return m + 1
