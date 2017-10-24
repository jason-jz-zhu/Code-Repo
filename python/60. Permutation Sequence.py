class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [1]
        for i in range(1, n + 1):
            fac.append(fac[-1] * i)

        nums = range(1, n + 1)
        res = []
        for i in range(n):
            rank = (k - 1) / fac[n - i - 1]
            k = (k - 1) % fac[n - i - 1] + 1
            res.append(nums[rank])
            nums.remove(nums[rank])
        return ''.join(str(d) for d in res)
