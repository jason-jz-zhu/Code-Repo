class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid * (mid + 1) / 2 == n:
                return mid
            elif mid * (mid + 1) / 2 < n:
                start = mid
            else:
                end = mid
        if start * (start + 1) / 2 < n:
            return start
        return end


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        curr = 1
        rem = n - 1
        while rem >= curr + 1:
            curr += 1
            rem -= curr
        return 0 if n == 0 else curr
