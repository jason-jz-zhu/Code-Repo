class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        import collections
        if nums is None or len(nums) < 2:
            return False

        hashmap = collections.defaultdict(int)
        hashmap[0] = -1
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if k:
                s %= k
            if s in hashmap:
                if (i - hashmap[s]) > 1:
                    return True
            else:
                hashmap[s] = i
        return False


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
