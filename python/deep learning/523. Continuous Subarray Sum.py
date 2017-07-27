class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums is None or len(nums) <= 1:
            return False

        for i in xrange(len(nums)):
            s = nums[i]
            for j in xrange(i + 1, len(nums)):
                s += nums[j]
                if s == k:
                    return True
                if k != 0 and s % k == 0:
                    return True
        return False


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s = 0
        hashmap = {0: -1}
        for i in xrange(len(nums)):
            s += nums[i]
            if k:
                s %= k
            if s in hashmap:
                if (i - hashmap[s]) > 1:
                    return True
            else:
                hashmap[s] = i
        return False
