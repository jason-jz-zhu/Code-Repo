class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return -1

        res = 0
        prev = 0
        curr = 0
        for i in range(len(nums)):
            if i > prev:
                prev = curr
                res += 1
            curr = max(curr, i + nums[i])
        return res
