class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        res = '-' if numerator * denominator < 0 else ''

        num = abs(numerator)
        denom = abs(denominator)
        carry = num // denom
        reminder = num % denom
        res += str(carry)
        if reminder == 0:
            return res
        else:
            res += '.'

        hashmap = {}
        i = len(res)
        while reminder != 0:
            if reminder not in hashmap:
                hashmap[reminder] = i
            else:
                i = hashmap[reminder]
                res = '{}({})'.format(res[: i], res[i:])
                return res
            reminder = reminder * 10
            res += str(reminder // denom)
            reminder %= denom
            i += 1
        return res
        
