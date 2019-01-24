class Solution:
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) < 7:
            return False
        n = len(nums)
        r_sum = [0 for _ in range(n)]
        r_sum[0] = nums[0]
        for i in range(1, n):
            r_sum[i] = r_sum[i - 1] + nums[i]

        for j in range(3, n - 3):
            s = set()
            for i in range(1, j - 1):
                if r_sum[i - 1] == r_sum[j - 1] - r_sum[i]:
                    s.add(r_sum[i - 1])

            for k in range(j + 1, n - 1):
                s3 = r_sum[k - 1] - r_sum[j]
                s4 = r_sum[n - 1] - r_sum[k]
                if s3 == s4 and s3 in s:
                    return True
        return False
