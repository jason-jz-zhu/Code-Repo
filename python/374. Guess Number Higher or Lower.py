# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start + 1 < end:
            mid = start + (end - start) / 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) < 0:
                end = mid
            else:
                start = mid
        if guess(start) == 0:
            return start
        return end
