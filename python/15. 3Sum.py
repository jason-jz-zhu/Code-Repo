class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Solution.res = []
        if nums is None or len(nums) < 3:
            return Solution.res

        nums.sort()

        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            self.two_sum(nums, left, right, target)
        return Solution.res

    def two_sum(self, nums, left, right, target):
        while (left < right):
            sum = nums[left] + nums[right]
            if sum == target:
                Solution.res.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif sum > target:
                right -= 1
            else:
                left += 1

            
