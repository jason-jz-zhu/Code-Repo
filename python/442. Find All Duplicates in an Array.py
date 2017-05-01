class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in xrange(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                res.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]
        return res
            
