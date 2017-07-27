class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a is None or b is None:
            return ''
        if len(a) == 0 or len(b) == 0:
            return a if len(a) != 0 else b

        idxA = len(a) - 1
        idxB = len(b) - 1

        carry = 0
        res = ''
        while idxA >= 0 or idxB >= 0:
            tmpA = int(a[idxA]) if idxA >= 0 else 0
            tmpB = int(b[idxB]) if idxB >= 0 else 0
            reminder = (tmpA + tmpB + carry) % 2
            carry = (tmpA + tmpB + carry) / 2
            if reminder == 0:
                res = '0' + res
            else:
                res = '1' + res
            idxA -= 1
            idxB -= 1
        if carry == 1:
            res = '1' + res
        return res
