class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ra, ia = map(int, a[:-1].split('+'))
        rb, ib = map(int, b[:-1].split('+'))
        return '{}+{}i'.format(ra * rb - ia * ib, ra * ib + ia * rb)
