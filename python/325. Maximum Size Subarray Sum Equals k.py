class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import collections
        if nums is None or len(nums) == 0:
            return 0

        hashmap = collections.defaultdict(int)
        hashmap[0] = -1
        s = res = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - k in hashmap:
                res = max(res, i - hashmap[s - k])
            if s not in hashmap:
                hashmap[s] = i
        if res == -sys.maxint - 1:
            return 0
        return res
