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
        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if s >= target:
                    end -= 1
                else:
                    res += (end - start)
                    start += 1
        return res
