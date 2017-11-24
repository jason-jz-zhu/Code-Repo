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
                    if tmp < 0:
                        stack.append(-(abs(tmp) / num))
                    else:
                        stack.append(tmp / num)

                sign = s[i]
                num = 0

        return sum(stack)


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        s = s.replace(' ', '')
        stack = []
        first_num = self.getNum(0, s)
        stack.append(int(first_num))
        i = len(first_num)

        while i < len(s):
            sign = s[i]
            num = self.getNum(i + 1, s)
            if sign == '+':
                stack.append(int(num))
            elif sign == '-':
                stack.append(-int(num))
            elif sign == '*':
                stack.append(stack.pop() * int(num))
            else:
                tmp = stack.pop()
                if tmp < 0:
                    stack.append(-(abs(tmp) / int(num)))
                else:
                    stack.append(tmp / int(num))
            i += len(num) + 1

        return sum(stack)

    def getNum(self, i, s):
        num = ''
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1

        return num
