from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        res = []
        if len(nums) < k or k == 0:
            return []

        for i, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()
            q.append(i)

            if q[0] == i - k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
