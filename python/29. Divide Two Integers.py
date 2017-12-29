class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        neg = (dividend * divisor) < 0
        a, b = abs(dividend), abs(divisor)
        res = 0
        while a >= b:
            tmp, cnt = b, 1
            while a >= tmp:
                a -= tmp
                res += cnt
                cnt <<= 1
                tmp <<= 1
        if neg:
            res = - res
        return INT_MAX if res > INT_MAX else res
