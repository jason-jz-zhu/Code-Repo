# using iteratively
# 从第一个元素开始，若其大于相邻的后续元素
# 则第一个元素就是一个局部最大值，返回即可。若其小于相邻的后续元素，
# 则第二个元素大于第一个元素。如此，一一遍历数组，第一次出现，
# 第i个元素若大于其相邻后续元素，则该元素就是一个局部最大值，返回即可
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(1, len(nums)):
            if nums[i] < nums[i-1]:
                return i - 1
        return len(nums) - 1

# using binary search
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid
        return start if nums[start] > nums[end] else end
