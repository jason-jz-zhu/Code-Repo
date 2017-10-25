class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        start, end = 1, n
        while start <= end:
            if k > 1:
                if k % 2 != 0:
                    res.append(start)
                    start += 1
                else:
                    res.append(end)
                    end -= 1
                k -= 1
            else:
                res.append(start)
                start += 1
        return res

            
