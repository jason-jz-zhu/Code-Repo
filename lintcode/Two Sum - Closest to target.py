class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumClosest(self, nums, target):
        # Write your code here
        diff = sys.maxint
        if nums is None and len(nums) < 2:
            return None
        nums.sort()
        left, right = 0, len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return 0
            elif sum > target:
                diff = min(diff, abs(target - sum))
                right -= 1
            else:
                diff = min(diff, abs(target - sum))
                left += 1

        return diff
