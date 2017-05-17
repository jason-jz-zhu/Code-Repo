class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        checker = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in checker:
                return False
            else:
                checker.add(n)
        return True
