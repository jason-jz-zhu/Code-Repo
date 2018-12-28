class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX = 2 ** 31 - 1
        MIN = 2 ** 31 * -1
        flag = -1 if (dividend * divisor) < 0 else 1
        res = 0
        a, b = abs(dividend), abs(divisor)
        while a >= b:
            tmp = b
            cnt = 1
            while tmp + tmp <= a:
                tmp += tmp
                cnt += cnt
            res += cnt
            a -= tmp
        if res * flag > MAX:
            return MAX
        elif res * flag < MIN:
            return MIN
        else:
            return res * flag
