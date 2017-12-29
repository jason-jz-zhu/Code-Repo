class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if houses is None or len(houses) == 0:
            return None
        if heaters is None or len(heaters) == 0:
            return None
        houses.sort()
        heaters.sort()
        res = [float('inf')] * len(houses)
        # For each house, calculate distance to nearest RHS heater
        r = k = 0
        while r < len(houses) and k < len(heaters):
            if houses[r] <= heaters[k]:
                res[r] = heaters[k] - houses[r]
                r += 1
            else:
                k += 1
        # For each house, calculate distance to nearest LHS heater
        l = len(houses) - 1
        k = len(heaters) - 1
        while l >= 0 and k >= 0:
            if houses[l] >= heaters[k]:
                res[l] = min(res[l], houses[l] - heaters[k])
                l -= 1
            else:
                k -= 1
        return max(res)

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if houses is None or len(houses) == 0:
            return None
        if heaters is None or len(heaters) == 0:
            return None
        houses.sort()
        heaters.sort()
        res = 0
        for house in houses:
            start, end = 0, len(heaters) - 1
            while start + 1 < end:
                mid = start + (end - start) / 2
                if heaters[mid] < house:
                    start = mid
                else:
                    end = mid
            dist1 = abs(heaters[end] - house)
            dist2 = abs(heaters[start] - house)
            res = max(res, min(dist1, dist2))
        return res
