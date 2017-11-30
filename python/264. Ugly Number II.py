class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        i2 = i3 = i5 = 0

        while len(res) < n:
            m2, m3, m5 = res[i2] * 2, res[i3] * 3, res[i5] * 5
            mm = min(m2, m3, m5)
            if mm == m2:
                i2 += 1
            if mm == m3:
                i3 += 1
            if mm == m5:
                i5 += 1
            res.append(mm)

        return res[-1]
