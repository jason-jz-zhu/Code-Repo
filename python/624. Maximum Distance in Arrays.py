class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        if arrays is None or len(arrays) < 2:
            return 0

        res = 0
        min_v, max_v = arrays[0][0], arrays[0][-1]
        for i in xrange(1, len(arrays)):
            res = max(res, abs(arrays[i][0] - max_v))
            res = max(res, abs(arrays[i][-1] - min_v))
            max_v = max(max_v, arrays[i][-1])
            min_v = min(min_v, arrays[i][0])

        return res



class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        if arrays is None or len(arrays) < 2:
            return 0

        # find the 1st min and 1st max along with their associated array indices in arrays
        min1, imin1 = min((array[0], i) for i, array in enumerate(arrays))
        max1, imax1 = max((array[-1], i) for i, array in enumerate(arrays))
        if imin1 != imax1:
            return max1 - min1
        # find the 2nd min and 2nd max
        min2 = min(array[0] for i, array in enumerate(arrays) if i != imin1)
        max2 = max(array[-1] for i, array in enumerate(arrays) if i != imax1)
        return max(max2 - min1, max1 - min2)
