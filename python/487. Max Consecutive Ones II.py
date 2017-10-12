class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        cnt = res = prev = 0
        for num in nums:
            cnt += 1
            if num == 0:
                prev = cnt
                cnt = 0
            res = max(res, cnt + prev)
        return res

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        left = zero = res = 0
        k = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            while zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            res = max(res, right - left + 1)
        return res

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import deque
        res = left = 0
        k = 1
        q = collections.deque([])
        for right in xrange(len(nums)):
            if nums[right] == 0:
                q.append(right)
            if len(q) > k:
                left = q.popleft() + 1
            res = max(res, right - left + 1)
        return res
