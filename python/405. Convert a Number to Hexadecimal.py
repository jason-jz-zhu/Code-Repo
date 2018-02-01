class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        res = ''
        hashmap = '0123456789abcdef'
        for _ in range(8):
            res = hashmap[(num & 15)] + res
            num = (num >> 4)
        return res.lstrip('0')
