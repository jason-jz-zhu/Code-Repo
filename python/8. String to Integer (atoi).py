class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str is None:
            return 0
        str = str.strip()
        if len(str) == 0:
            return 0

        res = 0
        sign = 1
        i = 0
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            sign = -1

        for j in range(i, len(str)):
            if not str[j].isdigit():
                break
            res = res * 10 + int(str[j])
            if res > float('inf'):
                break
        res *= sign
        if res >= 2 ** 31:
            return 2 ** 31 - 1
        if res <= -2 ** 31:
            return -2 ** 31
        return res
