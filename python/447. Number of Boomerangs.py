class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if points is None or len(points) < 3:
            return 0
        res, n = 0, len(points)

        for i in xrange(n):
            hash = {}
            # calculate how many j points to i point have same distance
            for j in xrange(n):
                dist = ((points[j][0] - points[i][0]) ** 2) + ((points[j][1] - points[i][1]) ** 2)
                hash[dist] = hash.get(dist, 0) + 1
            # loop hash
            for key, item in hash.iteritems():
                if item >= 2:
                    res += item * (item - 1)

        return res
            
