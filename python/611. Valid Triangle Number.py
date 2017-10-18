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
        for i in range(len(nums) - 1, 1, -1):
            start, end = 0, i - 1
            while start < end:
                s = nums[start] + nums[end]
                if s > nums[i]:
                    res += (end - start)
                    end -= 1
                else:
                    start += 1
        return res
