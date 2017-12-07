class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        hashmap = collections.defaultdict(int)
        hashmap[0] = -1

        r_sum = res = 0
        for i in range(len(nums)):
            r_sum += -1 if nums[i] == 0 else 1
            if r_sum in hashmap:
                res = max(res, i - hashmap[r_sum])
            else:
                hashmap[r_sum] = i
        return res
