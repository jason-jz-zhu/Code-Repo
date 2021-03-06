class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        cnt = res = 0
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 0
            res = max(res, cnt)
        return res
