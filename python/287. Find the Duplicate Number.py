class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1

        start, end = 1, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            cnt = sum(1 for num in nums if num <= mid)
            if mid < cnt:
                end = mid
            else:
                start = mid

        cnt = sum(1 for num in nums if num <= start)
        if start < cnt:
            return start
        return end


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) <= 1:
            return -1

        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
