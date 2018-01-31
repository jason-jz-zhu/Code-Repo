class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        tmp = bin(n)
        for i in range(3, len(tmp)):
            if tmp[i - 1] == tmp[i]:
                return False
        return True

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        last_bit = n % 2 # last bit
        n //= 2 # rest of bit
        while n:
            if last_bit == n % 2:
                return False
            last_bit = n % 2
            n //= 2
        return True

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        last_bit = n & 1
        n >>= 1
        while n:
            if last_bit == n & 1:
                return False
            last_bit = n & 1
            n >>= 1
        return True
            
