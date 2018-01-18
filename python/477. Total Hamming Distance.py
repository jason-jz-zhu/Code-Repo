class Solution:
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) < 2:
            return 0
        res = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                if (num >> i) & 1:
                    cnt += 1
            res += cnt * (len(nums) - cnt)
        return res
