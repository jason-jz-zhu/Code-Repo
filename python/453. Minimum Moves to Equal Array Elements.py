class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minVal, res = min(nums), 0
        for num in nums:
            res += num - minVal
        return res

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)
