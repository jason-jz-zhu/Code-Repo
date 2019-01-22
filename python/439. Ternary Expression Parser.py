class Solution:
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        res = expression
        stack = []
        for i in range(len(expression)):
            if expression[i] == '?':
                stack.append(i)

        while stack:
            tmp = stack.pop()
            res = res[: tmp - 1] + self.helper(res[tmp - 1: tmp + 4]) + res[tmp + 4:]
        return res

    def helper(self, s):
        if len(s) != 5:
            return ''
        return s[2] if s[0] == 'T' else s[4]


class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if not expression:
            return ''

        stack = []

        for c in expression[::-1]:
            if stack and stack[-1] == '?':
                stack.pop()
                first = stack.pop()
                stack.pop()
                second = stack.pop()

                if c == 'T':
                    stack.append(first)
                else:
                    stack.append(second)
            else:
                stack.append(c)
        return str(stack[-1])
