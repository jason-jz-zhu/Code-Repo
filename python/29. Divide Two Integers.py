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
        neg = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        a, b = abs(dividend), abs(divisor)
        res, shift = 0, 31
        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                res += 1 << shift
            shift -= 1
        if neg:
            res = - res
        if res > INT_MAX:
            return INT_MAX
        return res
