class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        res = 0
        for _ in range(32):
            if n & 1 == 1:
                res = (res << 1) + 1
            else:
                res = res << 1
            n >>= 1
        return res

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        tmp = '{0:032b}'.format(n)
        tmp = tmp[::-1]
        return int(tmp, 2)
