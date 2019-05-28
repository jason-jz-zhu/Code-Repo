class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if tokens is None or len(tokens) == 0:
            return float('inf')
        oper = ['+', '-', '*', '/']
        stack = []
        for i in range(len(tokens)):
            element = tokens[i]
            if element not in oper:
                stack.append(int(element))
            else:
                if stack:
                    b, a = stack.pop(), stack.pop()
                    tmp = 0
                    if element == '+':
                        tmp = a + b
                    elif element == '-':
                        tmp = a - b
                    elif element == '*':
                        tmp = a * b
                    else:
                        if a * b < 0 and a % b != 0:
                            tmp = a // b + 1
                        else:
                            tmp = a // b
                    stack.append(tmp)
        return stack[-1]
