class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        flag = False
        for i in range(31, -1, -1):
            if num & (1 << i):
                flag = True
            if flag:
                num ^= (1 << i)
        return num
