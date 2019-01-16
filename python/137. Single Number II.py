class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None

        a = b = 0
        for num in nums:
            b = (b ^ num) & ~a
            a = (a ^ num) & ~b
        return b


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None

        res = 0
        for i in range(32):
            s = 0
            for j in range(len(nums)):
                s += (nums[j] >> i) & 1
            res |= (s % 3) << i
        return self.convert(res)

    def convert(self,x):
        if x >= 2**31:
            x -= 2**32
        return x


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None
        nums_set = set(nums)
        diff = sum(nums_set) * 3 - sum(nums)
        return diff // 2
