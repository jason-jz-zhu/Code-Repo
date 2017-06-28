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
        n = len(nums)
        res = n + 1
        left = right = sum = 0
        while right < n:
            while right < n and sum < s:
                sum += nums[right]
                right += 1

            if sum < s: break
            while left < right and sum >= s:
                res = min(res, right - left)
                sum -= nums[left]
                left += 1
        return 0 if res == n+1 else res

#  nlog(n)
