class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        # Write your code here
        l = len(nums)
        if nums is None or len(nums) == 0:
            return []
        if l < k or k <= 0:
            return []
        sums = [0 for i in xrange(l - k + 1)]
        # cal sums[0]
        for i in xrange(k):
            sums[0] += nums[i]

        # cal sums using pre sums
        for i in xrange(1, l - k + 1):
            sums[i] = sums[i - 1] - nums[i - 1] + nums[i - 1 + k]

        return sums
