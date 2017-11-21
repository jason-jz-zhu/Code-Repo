class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        num = 0
        sign = '+'
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp < 0 and tmp % num != 0:
                        stack.append(tmp / num + 1)
                    else:
                        stack.append(tmp / num)

                sign = s[i]
                num = 0

        return sum(stack)
