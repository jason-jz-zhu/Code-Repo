class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1
        import collections
        s = res = 0
        hashmap = collections.defaultdict(int)
        hashmap[0] = 1
        for num in nums:
            s += num
            if s - k in hashmap:
                res += hashmap[s - k]
            hashmap[s] += 1
        return res
