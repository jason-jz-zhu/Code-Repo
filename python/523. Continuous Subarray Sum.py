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
            
        for start in range(len(nums)):
            s = nums[start]
            for end in range(start + 1, len(nums)):
                s += nums[end]
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
        if nums is None or len(nums) <= 1:
            return False
        res = 0
        cs = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            cs[i] = nums[i - 1] + cs[i - 1]
        for start in range(len(nums)):
            for end in range(start + 2, len(nums) + 1):
                tmp = cs[end] - cs[start]
                if tmp == k or (k != 0 and tmp % k == 0):
                    return True
        return False
