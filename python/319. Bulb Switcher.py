class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n ** 0.5)


class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 1
        while res * res <= n:
            res += 1
        return res - 1
