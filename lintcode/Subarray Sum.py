class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return
        map = {0: -1}
        sum = 0
        for i in xrange(len(nums)):
            sum += nums[i]
            if sum in map:
                return [map[sum] + 1, i]
            map[sum] = i
        return
