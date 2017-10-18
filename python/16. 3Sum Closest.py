class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or len(nums) < 3:
            return None

        nums.sort()
        res = sys.maxint
        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                if abs(s - target) < abs(res):
                    res = s - target
                if s == target:
                    return s
                elif s < target:
                    start += 1
                else:
                    end -= 1
        return res + target
