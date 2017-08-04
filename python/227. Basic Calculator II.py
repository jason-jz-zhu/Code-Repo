class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return "0"
        res = num = 0
        sign = '+'
        nums = []
        for i in xrange(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
                if sign == '+':
                    nums.append(num)
                elif sign == '-':
                    nums.append(-num)
                elif sign == '*':
                    nums.append(nums.pop() * num)
                else:
                    tmp = nums.pop()
                    if tmp / num < 0 and tmp % num != 0:
                        nums.append(tmp / num+1)
                    else:
                        nums.append(tmp / num)
                sign = s[i]
                num = 0

        return sum(nums)
