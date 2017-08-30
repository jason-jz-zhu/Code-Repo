class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        f = lambda x, a, b, c: a * x * x + b * x + c

        res = []
        if not nums:
            return res

        left, right = 0, len(nums) - 1
        d = -1 if a > 0 else 1
        while left <= right:
            if d * f(nums[left], a, b, c) < d * f(nums[right], a, b, c):
                res.append(f(nums[left], a, b, c))
                left += 1
            else:
                res.append(f(nums[right], a, b, c))
                right -= 1
        return res[::d]
