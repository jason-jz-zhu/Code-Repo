class Solution:
    # @param nums {int[]} a list of integers
    # @param k {int} size of window
    # @return {int[]} the sum of element inside the window at each moving
    def winSum(self, nums, k):
        # Write your code here
        # check nums
        if nums is None or len(nums) == 0:
            return []

        l = len(nums)
        # check k
        if l < k or k <=0:
            return []
        # init the container of result
        sums = [0 for _ in xrange(l - k + 1)]
        # cal the sums[0]
        for i in xrange(k):
            sums[0] += nums[i]
        # cal rest of sums
        for i in xrange(1, l - k + 1):
            sums[i] = sums[i - 1] - nums[i - 1] + nums[i - 1 + k]

        return sums
