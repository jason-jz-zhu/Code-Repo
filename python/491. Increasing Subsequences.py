class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        import itertools
        return [x
                for i in xrange(2, len(nums) + 1)
                for x in set(itertools.combinations(nums, i))
                if all(a <= b for a, b in zip(x, x[1:]))]
