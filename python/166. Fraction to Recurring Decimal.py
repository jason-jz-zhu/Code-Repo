class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        negativeFlag = (numerator * denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        numList = []
        cnt = 0
        loopMap = {}
        loopStr = None
        while True:
            numList.append(str(numerator / denominator))
            cnt += 1
            numerator = 10 * (numerator % denominator)
            if numerator == 0:
                break
            loopExist = loopMap.get(numerator)
            if loopExist:
                loopStr = ''.join(numList[loopExist: cnt])
                break
            loopMap[numerator] = cnt
        res = numList[0]
        if len(numList) > 1:
            res += '.'
        if loopStr:
            res += ''.join(numList[1: len(numList) - len(loopStr)]) + '(' + loopStr + ')'
        else:
            res += ''.join(numList[1:])
        if negativeFlag:
            res = '-' + res
        return res
