class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections
        if nums is None or len(nums) == 0:
            return 0

        hashmap = collections.defaultdict(int)
        hashmap[0] = 1
        s = res = 0
        for num in nums:
            s += num
            if s - k in hashmap:
                res += hashmap[s - k]
            hashmap[s] += 1
        return res


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        for start in range(len(nums)):
            s = 0
            for end in range(start, len(nums)):
                s += nums[end]
                if s == k:
                    res += 1
        return res


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        cs = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            cs[i] = nums[i - 1] + cs[i - 1]
        for start in range(len(nums)):
            for end in range(start + 1, len(nums) + 1):
                if cs[end] - cs[start] == k:
                    res += 1
        return res
