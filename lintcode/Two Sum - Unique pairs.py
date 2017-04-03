class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum6(self, nums, target):
        # Write your code here
        if nums is None or len(nums) < 2:
            return 0
        nums.sort()
        res = 0
        left, right = 0, len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                res += 1
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
        return res
