class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        nums = list(range(1, n + 1))
        fac = [1] * n
        for i in range(1, n):
            fac[i] = fac[i - 1] * i
        k -= 1
        for i in range(n, 0, -1):
            rank = k // fac[i - 1]
            k = k % fac[i - 1]
            res.append(nums[rank])
            nums.remove(nums[rank])
        return ''.join(str(d) for d in res)
