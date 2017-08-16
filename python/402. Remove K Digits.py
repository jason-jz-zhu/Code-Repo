class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res = []
        n = k
        for d in num:
            while n and res and res[-1] > d:
                res.pop()
                n -= 1
            res.append(d)
        res = res[0: len(num) - k]
        res = ''.join(res).lstrip('0')
        return res if res else '0'
