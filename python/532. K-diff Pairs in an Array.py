class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) == 0 or k < 0:
            return 0

        import collections
        counter = collections.Counter(nums)
        res = 0
        for key, val in counter.iteritems():
            if k == 0:
                if val > 1:
                    res += 1
            else:
                if key + k in counter:
                    res += 1
        return res




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
        nums.sort()
        l = r = 0
        size = len(nums)
        while l < size and r < size:
            if l == r or nums[r] - nums[l] < k:
                r += 1
            elif nums[r] - nums[l] > k:
                l += 1
            else:
                l += 1
                res += 1
                while l < size and nums[l] == nums[l - 1]:
                    l += 1
                r = max(l + 1, r + 1)
        return res
