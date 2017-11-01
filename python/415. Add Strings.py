class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 is None or num2 is None:
            return ''
        if len(num1) == 0 or len(num2) == 0:
            return num1 if len(num1) != 0 else num2

        index_a, index_b = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ''
        while index_a >= 0 or index_b >= 0 or carry:
            if index_a >= 0:
                carry += ord(num1[index_a]) - ord('0')
                index_a -= 1
            if index_b >= 0:
                carry += ord(num2[index_b]) - ord('0')
                index_b -= 1
            remainder = carry % 10
            carry /= 10
            res = str(remainder) + res
        return res
