class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) < 3:
            return 0

        nums.sort()
        res = 0
        for i in xrange(len(nums) - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += (right - left)
                    right -= 1
                else:
                    left += 1
        return res
