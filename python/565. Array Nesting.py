class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        res = 0
        for num in nums:
            if num != None:
                start, cnt = num, 0
                while nums[start] != None:
                    tmp = start
                    start = nums[start]
                    nums[tmp] = None
                    cnt += 1
                res = max(res, cnt)
        return res
