class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = -(-len(B) / len(A))
        # times = int(math.ceil(float(len(B)) / len(A)))
        for i in range(2):
            tmp = A * (times + i)
            if B in tmp:
                return times + i
        return -1
