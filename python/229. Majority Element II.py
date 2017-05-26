class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return []
        size = len(nums)
        m1 = m2 = None
        c1 = c2 = 0
        for num in nums:
            if m1 == num:
                c1 += 1
            elif m2 == num:
                c2 += 1
            elif c1 == 0:
                m1, c1 = num, 1
            elif c2 == 0:
                m2, c2 = num, 1
            else:
                c1 -= 1
                c2 -= 1
        return [m for m in (m1, m2) if m is not None and nums.count(m) > size / 3]
