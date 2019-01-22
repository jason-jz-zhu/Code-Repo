class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        return any(self.isInt(c - a * a) for a in range(int(c ** 0.5) + 1))

    def isInt(self, b):
        return int(b ** 0.5) ** 2 == b
