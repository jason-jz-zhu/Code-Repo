class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if nums is None or len(nums) < k:
            return -sys.maxint
        run_sum = [0]
        for num in nums:
            run_sum.append(num + run_sum[-1])

        res = max([run_sum[i + k] - run_sum[i] for i in xrange(len(nums) - k + 1)])
        return res / float(k)
