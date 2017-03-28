class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if nums is None:
            return 0

        maxsofar = max_cur = nums[0]
        for num in nums[1:]:
            max_cur = max(num, max_cur + num)
            maxsofar = max(maxsofar, max_cur)

        return maxsofar
