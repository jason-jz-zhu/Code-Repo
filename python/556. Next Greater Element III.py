import numpy as np
class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return -1

        s = [int(e) for e in list(str(n))]

        left = -1
        for i in range(len(s) - 2, -1, -1):
            if s[i] < s[i + 1]:
                left = i
                break
        if left == -1:
            return -1

        right = left
        for j in range(len(s) - 1, left, -1):
            if s[j] > s[left]:
                right = j
                break
        s[left], s[right] = s[right], s[left]
        s[left + 1:] = reversed(s[left + 1:])
        res = int(''.join([str(num) for num in s]))
        return -1 if res > 2 ** 31 -1 else res
