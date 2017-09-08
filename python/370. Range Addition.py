class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        if length == 0:
            return []
        if updates is None or len(updates) == 0:
            return [0] * length

        res = [0] * length

        for update in updates:
            start, end, inc = update
            res[start] += inc
            if end + 1 < length:
                res[end + 1] -= inc

        for i in xrange(1, length):
            res[i] += res[i - 1]

        return res
