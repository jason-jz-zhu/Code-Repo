class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False
        for a in range(int(c ** 0.5) + 1):
            b = int((c - a ** 2) ** 0.5)
            if a ** 2 + b ** 2 == c:
                return True
        return False
