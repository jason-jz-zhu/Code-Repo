class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False
        cnt = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                cnt += 1
                if i == 0:
                    nums[i] = nums[i + 1]
                elif nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i + 1] = nums[i]
            if cnt > 1:
                return False
        return True
