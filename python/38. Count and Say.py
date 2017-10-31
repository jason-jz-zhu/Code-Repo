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

        for i in range(2, n + 1):
            tmp = pre
            pre = ''
            cnt = 1
            for j in range(1, len(tmp)):
                if tmp[j] == tmp[j - 1]:
                    cnt += 1
                else:
                    pre += str(cnt) + tmp[j - 1]
                    cnt = 1
            pre += str(cnt) + tmp[-1]
        return pre
