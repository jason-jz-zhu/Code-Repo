
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums is None or len(nums) < 7:
            return False
        size = len(nums)
        r_sum = [0] * size
        r_sum[0] = nums[0]
        for i in range(1, size):
            r_sum[i] += r_sum[i - 1] + nums[i]

        for j in range(3, size - 3):
            s = set()
            for i in range(1, j - 1):
                if r_sum[i - 1] == r_sum[j - 1] - r_sum[i]:
                    s.add(r_sum[i - 1])

            for k in range(j + 1, size - 1):
                s3 = r_sum[k - 1] - r_sum[j]
                s4 = r_sum[size - 1] - r_sum[k]
                if s3 == s4 and s3 in s:
                    return True
        return False
