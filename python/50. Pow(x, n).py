class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return self.myPow(x*x, n/2) * x
        else:
            return self.myPow(x*x, n/2)


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        p = 1
        while n:
            if n % 2 != 0:
                p *= x
            x *= x
            n = n / 2
        return p



class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        p = 1
        while n:
            if n & 1:
                p *= x
            x *= x
            n >>= 1
        return p
