class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        res = 0
        n = len(heaters)
        houses.sort()
        heaters.sort()
        for house in houses:
            start, end = 0, n - 1
            while start + 1 < end:
                mid = start + (end - start) / 2
                if heaters[mid] < house:
                    start = mid
                else:
                    end = mid
            dist1 = abs(heaters[end] - house)
            dist2 = abs(house - heaters[start])
            res = max(res, min(dist1, dist2))
        return res
