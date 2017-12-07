class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return ''
        flag = -1 if numerator * denominator < 0 else 1
        numerator = abs(numerator)
        denominator = abs(denominator)
        loop_str = ''
        idx = 0
        hashmap = collections.defaultdict(int)
        pool = []
        while True:
            pool.append(str(numerator / denominator))
            idx += 1
            numerator = 10 * (numerator % denominator)
            if numerator == 0:
                break
            loop_exit = hashmap[numerator]
            if loop_exit:
                loop_str = ''.join(pool[loop_exit: idx])
                break
            hashmap[numerator] = idx
        res = pool[0]
        if len(pool) > 1:
            res += '.'
        if loop_str:
            res += ''.join(pool[1: len(pool) - len(loop_str)]) + '(' + loop_str + ')'
        else:
            res += ''.join(pool[1:])
        if flag == -1:
            res = '-' + res
        return res
        
