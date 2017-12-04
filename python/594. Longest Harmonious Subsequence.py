class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        hashmap = collections.Counter(nums)
        res = 0

        for key in hashmap.keys():
            if key + 1 in hashmap:
                res = max(res, hashmap[key] + hashmap[key + 1])
        return res
