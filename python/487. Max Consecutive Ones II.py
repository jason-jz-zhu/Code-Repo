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

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = zero = left = 0
        k = 1
        for right in xrange(len(nums)):
            if nums[right] == 0:
                zero += 1
            while zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            res = max(res, right -left + 1)
        return res


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = cnt = cur = 0
        for num in nums:
            cnt += 1
            if num == 0:
                cur = cnt
                cnt = 0
            res = max(res, cur + cnt)
        return res
