class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None or len(A) == 0 or len(A[0]) == 0:
            return None
        if B is None or len(B) == 0 or len(B[0]) == 0:
            return None

        res = [[0 for i in xrange(len(B[0]))] for j in xrange(len(A))]

        for i in xrange(len(A)):
            for k in xrange(len(A[0])):
                if A[i][k] != 0:
                    for j in xrange(len(B[0])):
                        if B[k][j] != 0:
                            res[i][j] += A[i][k] * B[k][j]
        return res
