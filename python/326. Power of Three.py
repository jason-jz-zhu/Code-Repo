class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n != 1:
            if n % 3 != 0:
                return False
            n /= 3
        return True


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        return n % 3 == 0 and self.isPowerOfThree(n / 3)


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n <= 0 else n == round(3 ** round(math.log(n, 3)))
