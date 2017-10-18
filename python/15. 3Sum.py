class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 3:
            return []

        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                s = nums[start] + nums[end]
                if s == target:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif s < target:
                    start += 1
                else:
                    end -= 1
        return res
