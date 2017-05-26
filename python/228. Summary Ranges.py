class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums is None or len(nums) == 0:
            return []

        res = []
        l = len(nums)
        end = 0
        while end < l:
            start = end
            while end < l - 1 and nums[end] + 1 == nums[end + 1]:
                end += 1
            if nums[start] != nums[end]:
                res.append(str(nums[start]) + '->' + str(nums[end]))
            else:
                res.append(str(nums[start]))
            end += 1
        return res
        
