class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        start, end = 1, n
        while start + 1 < end:
            mid = start + (end - start) / 2
            tmp = mid * (mid + 1) / 2
            if tmp == n:
                return mid
            elif tmp < n:
                start = mid
            else:
                end = mid
        return start if start * (start + 1) / 2 < n else end


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        curr = 1
        rest = n - 1
        while rest >= curr + 1:
            curr += 1
            rest -= curr
        return curr
