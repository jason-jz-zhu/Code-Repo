class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        res = 1
        for d in b:
            res = self.myPow(res, 10, 1337) * self.myPow(a, d, 1337) % 1337
        return res

    def myPow(self, a, n, m):
        if n == 0:
            return 1
        res = 1
        while n:
            if n % 2 != 0:
                res *= a
            a *= a
            n = n / 2
        return res % m


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        res = 1
        for d in b:
            res = self.myPow(res, 10, 1337) * self.myPow(a, d, 1337) % 1337
        return res

    def myPow(self, a, n, m):
        if n == 0:
            return 1
        if n == 1:
            return a % 1337
        return self.myPow(a % 1337, n / 2, 1337) * self.myPow(a % 1337, n - n / 2, 1337) % 1337
