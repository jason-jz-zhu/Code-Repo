class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 is None or num2 is None:
            return None

        l1, l2 = len(num1), len(num2)
        l3 = l1 + l2
        num3 = [0 for _ in xrange(l3)]
        for i in xrange(l1-1, -1, -1):
            carry = 0
            for j in xrange(l2-1, -1, -1):
                product = carry + num3[i+j+1] + (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                num3[i+j+1] = product % 10
                carry = product / 10
            j = -1
            num3[i+j+1] = carry


        i = 0
        while i < l3 - 1 and num3[i] == 0:
            i += 1
        return ''.join(str(x) for x in num3[i:])
