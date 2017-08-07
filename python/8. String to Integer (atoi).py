class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == '':
            return 0
        i = res = 0
        sign = 1
        INT_MAX =  2147483647
        INT_MIN = -2147483648
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            sign = -1

        for idx in xrange(i, len(str)):
            if str[idx] < '0' or str[idx] > '9':
                break
            res = res * 10 + int(str[idx])
            if res > INT_MAX:
                break
        res *= sign
        if res >= INT_MAX:
            return INT_MAX
        if res <= INT_MIN:
            return INT_MIN
        return res
