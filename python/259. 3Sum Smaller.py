class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) < 3:
            return 0
        nums.sort()
        res = 0
        for i in xrange(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s >= target:
                    right -= 1
                else:
                    res += right - left
                    left += 1
        return res
