class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if tokens is None or len(tokens) == 0:
            return None
        op = ['+', '-', '*', '/']
        stack = []

        for token in tokens:
            if token not in op:
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                stack.append(self.calculate(x, y, token))
        return stack[0]

    def calculate(self, x, y, op):
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        else:
            return int(x * 1.0 / y)
