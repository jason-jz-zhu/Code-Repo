class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        hashmap = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        l = len(num)
        for i in xrange((l + 1) / 2):
            if num[l-1-i] not in hashmap or \
                num[i] != hashmap[num[l-1-i]]:
                    return False
        return True
