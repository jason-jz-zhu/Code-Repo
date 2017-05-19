class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) == 0 or k < 0:
            return 0
        res = 0
        hash = {}

        # init hash
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
        # regular search in the hash
        for key, value in hash.iteritems():
            if k == 0:
                if value >= 2:
                    res += 1
            else:
                if hash.get((key + k), False):
                    res += 1
        return res
