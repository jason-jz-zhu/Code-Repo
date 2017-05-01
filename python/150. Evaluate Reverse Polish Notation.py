class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if tokens is None or len(tokens) == 0:
            return None
        op = ['+', '-', '*', '/']
        s = []

        for token in tokens:
            if token not in op:
                s.append(int(token))
            else:
                y = s.pop()
                x = s.pop()
                s.append(self.evaluate(x, y, token))
        return s[0]


    def evaluate(self, x, y, op):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        else:
            return int(x * 1.0 / y)
