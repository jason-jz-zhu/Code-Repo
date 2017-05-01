class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 1, len(nums) - 1
        while start + 1 < end:
            mid = (end - start) / 2 + start
            if self.check_smaller_cnt(mid, nums) <= mid:
                start = mid
            else:
                end = mid

        if self.check_smaller_cnt(start, nums) <= start:
            return end
        return start

    def check_smaller_cnt(self, mid, nums):
        cnt = 0
        for num in nums:
            if num <= mid:
                cnt += 1
        return cnt

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return -1

        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        finder = 0
        while slow != finder:
            finder = nums[finder]
            slow = nums[slow]

        return slow
