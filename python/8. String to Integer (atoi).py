class Solution(object):
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

        i = res = 0
        sign = 1
        INT_MAX = sys.maxint
        INT_MIN = -sys.maxint - 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            sign = -1

        for idx in range(i, len(str)):
            if not str[idx].isdigit():
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
        
