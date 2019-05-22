class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = len(nums)
        dp_max = [1] * m
        dp_min = [1] * m
        dp_max[0] = dp_min[0] = nums[0]
        res = nums[0]
        for i in range(1, m):
            dp_max[i] = max(nums[i], max(nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]))
            dp_min[i] = min(nums[i], min(nums[i] * dp_max[i - 1], nums[i] * dp_min[i - 1]))
            res = max(res, dp_max[i], dp_min[i])
        return res

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = len(nums)
        dp_max = [1, 1]
        dp_min = [1, 1]
        dp_max[0] = dp_min[0] = nums[0]
        res = nums[0]
        now, old = 0, 1
        for i in range(1, m):
            now, old = old, now
            dp_max[now] = max(nums[i], max(nums[i] * dp_max[old], nums[i] * dp_min[old]))
            dp_min[now] = min(nums[i], min(nums[i] * dp_max[old], nums[i] * dp_min[old]))
            res = max(res, dp_max[now], dp_min[now])
        return res
