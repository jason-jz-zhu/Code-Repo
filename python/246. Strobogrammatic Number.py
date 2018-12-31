class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        hashmap = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        size = len(num)
        for i in range((size + 1) // 2):
            if num[size - 1 - i] not in hashmap or num[i] != hashmap[num[size- 1- i]]:
                return False
        return True
