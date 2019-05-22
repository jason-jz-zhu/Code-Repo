class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        m = len(nums)
        res = cnt = 1
        for i in range(1, m):
            if nums[i - 1] < nums[i]:
                cnt += 1
            else:
                cnt = 1
            res = max(res, cnt)
        return res
