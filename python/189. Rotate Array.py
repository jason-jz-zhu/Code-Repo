class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return

        l = len(nums)
        k = k % len(nums)
        self.reverse(nums, 0, l -1 - k)
        self.reverse(nums, l - k, l - 1)
        self.reverse(nums, 0, l - 1)

    def reverse(self, nums, start , end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return
        l = len(nums)
        k = k % l
        f_part = nums[: l - k]
        s_part = nums[l - k:]
        nums[:] = s_part + f_part


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None or len(nums) == 0:
            return

        l = len(nums)
        idx = 0
        cur = nums[0]
        distance = 0

        for _ in range(l):
            idx = (idx + k) % l
            nums[idx], cur = cur, nums[idx]

            distance = (distance + k) % l
            if distance == 0:
                idx = (idx + 1) % l
                cur = nums[idx]
