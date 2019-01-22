class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        res = ''
        cnt = 0
        while len(res) < len(B):
            res += A
            cnt += 1
        if B in res:
            return cnt
        res += A
        if B in res:
            return cnt + 1
        return -1
