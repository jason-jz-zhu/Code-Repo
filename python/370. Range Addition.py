class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        if length == 0 or updates is None or len(updates) == 0 or len(updates[0]) == 0:
            return [0] * length

        res = [0] * length
        for update in updates:
            start, end, inc = update
            res[start] += inc
            if end + 1 < length:
                res[end + 1] -= inc

        for i in range(1, length):
            res[i] += res[i - 1]

        return res
