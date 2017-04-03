class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum5(self, nums, target):
        # Write your code here
        if nums is None or len(nums) < 2:
            return 0

        nums.sort()

        res = 0
        left, right = 0, len(nums) - 1
        # main
        while left < right:
            sum = nums[left] + nums[right]
            if sum > target:
                right -= 1
            else:
                res += right - left
                left += 1

        return res
