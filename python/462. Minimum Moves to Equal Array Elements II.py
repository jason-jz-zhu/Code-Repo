class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        nums.sort()
        median = nums[len(nums) / 2]
        return sum(abs(num - median) for num in nums)
