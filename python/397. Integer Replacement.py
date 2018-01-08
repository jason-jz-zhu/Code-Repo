class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n % 2:
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
        else:
            return 1 + self.integerReplacement(n/2)

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        res = 0
        while n > 1:
            res += 1
            if n % 2 == 0:
                n /= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return res
