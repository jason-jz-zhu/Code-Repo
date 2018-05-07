class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start, end = 1, num
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if mid * mid == num:
                return True
            elif mid * mid < num:
                start = mid + 1
            else:
                end = mid - 1
        if start * start == num:
            return True
        if end * end == num:
            return True
        return False
