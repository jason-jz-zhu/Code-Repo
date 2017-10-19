# log(n)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        r_sum = start = end = 0
        res = float('inf')
        while end < len(nums):
            if r_sum < s:
                r_sum += nums[end]
            end += 1
            while r_sum >= s:
                res = min(res, end - start)
                r_sum -= nums[start]
                start += 1

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
