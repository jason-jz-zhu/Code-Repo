class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        if left < 1 or right > 10000 or left > right:
            return []
        res = []
        for i in range(left, right + 1):
            if self.helper(i):
                res.append(i)
        return res

    def helper(self, num):
        tmp = str(num)
        for c in tmp:
            if c == '0' or num % int(c) != 0:
                return False
        return True
