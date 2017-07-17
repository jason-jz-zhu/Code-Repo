class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ''

        if n == 1:
            return '1'

        pre = '1'

        for i in xrange(2, n + 1):
            tmp = pre
            pre = ''
            count = 1
            for j in xrange(1, len(tmp)):
                if tmp[j] == tmp[j - 1]:
                    count += 1
                else:
                    pre += str(count) + tmp[j - 1]
                    count = 1

            pre += str(count) + tmp[-1]
        return pre
