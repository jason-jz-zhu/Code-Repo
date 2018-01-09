class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        ints = map(int, re.findall('[+-]?\d+', expression))
        A, B = 0, 1
        for a in ints:
            b = next(ints)
            A = A * b + a * B
            B *= b
            g = self.gcd(A, B)
            A //= g
            B //= g
        return '{}/{}'.format(A, B)

    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)
