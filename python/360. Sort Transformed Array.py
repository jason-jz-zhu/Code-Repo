class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []
        res = []
        left, right = 0, len(nums) - 1
        d = -1 if a > 0 else 1
        while left <= right:
            left_val = self.helper(nums[left], a, b, c)
            right_val = self.helper(nums[right], a, b, c)
            if d * left_val < d * right_val:
                res.append(left_val)
                left += 1
            else:
                res.append(right_val)
                right -= 1
        return res[::d]

    def helper(self, x, a, b, c):
        return a * x * x + b * x + c
