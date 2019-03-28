# log(n)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        res = float('inf')
        left = right = 0
        windows_sum = 0
        while right < len(nums):
            windows_sum += nums[right]
            while left <= right and windows_sum >= s:
                res = min(res, right - left + 1)
                windows_sum -= nums[left]
                left += 1
            right += 1
        return 0 if res == float('inf') else res

#  nlog(n)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        size = len(nums)
        res = size + 1
        sm = [n for n in nums]
        for i in xrange(1, size):
            sm[i] += sm[i-1]

        for i in xrange(size):
            target = s + sm[i] - nums[i]
            end = self.binarySearch(sm, i, size, target)
            if end < size:
                res = min(res, end-i+1)

        return res if res != size + 1 else 0

    def binarySearch(self, sm, start, end, target):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if sm[mid] == target:
                return mid
            elif sm[mid] < target:
                start = mid
            else:
                end = mid
        if sm[start] >= target:
            return start
        return end
