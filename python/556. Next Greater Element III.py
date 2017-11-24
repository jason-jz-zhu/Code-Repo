import numpy as np
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return -1

        s = map(int, list(str(n)))
        size = len(s)
        left = -1

        for i in range(size - 2, -1, -1):
            if s[i] < s[i + 1]:
                left = i
                break

        if left == -1:
            return -1

        right = left
        for j in range(size - 1, left, -1):
            if s[j] > s[left]:
                right = j
                break

        s[left], s[right] = s[right], s[left]
        s[left + 1:] = reversed(s[left + 1: len(s)])

        res = int(''.join(map(str, s)))
        return -1 if res >= np.iinfo('int32').max else res
