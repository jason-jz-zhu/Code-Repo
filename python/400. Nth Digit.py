class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return None
        start, cnt, l = 1, 9, 1
        while n > l * cnt:
            n -= l * cnt
            l += 1
            cnt *= 10
            start *= 10
        start += (n - 1) / l
        tmp = str(start)
        return int(tmp[(n - 1) % l])
