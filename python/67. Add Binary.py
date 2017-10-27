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

        index_a, index_b = len(a) - 1, len(b) - 1
        res = ''
        carry = 0

        while index_a >= 0 or index_b >= 0 or carry:
            if index_a >= 0:
                carry += int(a[index_a])
                index_a -= 1

            if index_b >= 0:
                carry += int(b[index_b])
                index_b -= 1

            reminder = carry % 2
            carry = carry / 2
            res = str(reminder) + res
        return res
