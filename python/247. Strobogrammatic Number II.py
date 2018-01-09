class Solution(object):
    lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n, n)

    def helper(self, n, k):
        if k == 0:
            return ['']
        if k == 1:
            return ['0', '1', '8']
        res = []
        for num in self.helper(n, k - 2):
            for key, val in self.lookup.items():
                if n != k or key != '0':
                    res.append(key + num + val)
        return res
