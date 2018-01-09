class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        if equation is None or len(equation) == 0:
            return ''
        x = a = 0
        side = 1
        for eq, sign, num, isx in re.findall('(=)|([-+]?)(\\d*)(x?)', equation):
            if eq:
                side = -1
            elif isx:
                x += side * int(sign + '1') * int(num or 1)
            elif num:
                a -= side * int(sign + num)
        return 'x={}'.format(a / x) if x else 'No solution' if a else 'Infinite solutions' 
