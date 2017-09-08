class Solution(object):
    def trailingZeroes(self, n):
        res = 0
        while n > 0:
            res += n / 5
            n /= 5
        return res


class Solution(object):
    def trailingZeroes(self, n):
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)
