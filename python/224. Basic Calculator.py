class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        num = 0
        sign = 1
        stack = []
        for ss in s:
            if ss.isdigit():
                num = num * 10 + int(ss)
            elif ss == '+':
                res += sign * num
                num = 0
                sign = 1
            elif ss == '-':
                res += sign * num
                num = 0
                sign = -1
            elif ss == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ss == ')':
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num * sign
