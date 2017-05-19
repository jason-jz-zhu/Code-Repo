class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) == 0 or len(nums[0]) == 0:
            return nums
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        res = [[0 for i in xrange(c)] for j in xrange(r)]
        for i in xrange(r * c):
            # use this model to do the mapping
            res[i / c][i % c] = nums[i / n][i % n]
        return res
