class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops is None or len(ops) == 0 or len(ops[0]) == 0:
            return m * n

        for op in ops:
            m = min(m, op[0])
            n = min(n, op[1])

        return m * n
