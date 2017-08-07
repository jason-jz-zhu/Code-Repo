import numpy as np
class Solution(object):

    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = map(int, list(str(n)))
        left, right = -1, 0
        for i in xrange(len(s) - 1, 0, -1):
            if s[i] > s[i - 1]:
                left = i - 1
                break
        if left == -1:
            return -1

        for j in xrange(len(s) - 1, left, -1):
            if s[j] > s[left]:
                right = j
                break
        s[left], s[right] = s[right], s[left]
        s[left + 1:] = reversed(s[left + 1: len(s)])
        res = int(''.join(map(str, s)))
        return -1 if res >= np.iinfo('int32').max else res

                
