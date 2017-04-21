class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        start, end = 1, x
        while start + 1 < end:
            mid = (end - start) / 2 + start
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid

        if end * end < x:
            return int(end)
        return int(start)
