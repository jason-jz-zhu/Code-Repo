class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        maxPowerOfThree = pow(3, 19)
        return (n > 0 and maxPowerOfThree % n == 0)
