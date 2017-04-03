class Solution:
    # @param {int[]} nums an array of integers
    # @return {int} the number of unique integers
    def deduplication(self, nums):
        # Write your code here
        if len(nums) == 0:
            return 0

        nums.sort()

        end = 0
        for i in xrange(len(nums)):
            if nums[end] != nums[i]:
                end += 1
                nums[end] = nums[i]

        return end + 1
