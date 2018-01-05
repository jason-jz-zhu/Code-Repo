class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # F(i) = F(i-1) + sum - n*A[n-i]
        s = tmp = 0
        size = len(A)
        for i in range(size):
            s += A[i]
            tmp += i * A[i]
        res = tmp
        for i in range(1, size):
            tmp = tmp + s - size * A[size - i]
            res = max(res, tmp)
        return res
