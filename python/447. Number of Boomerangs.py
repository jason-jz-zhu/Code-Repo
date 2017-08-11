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
            hashmap = collections.defaultdict(int)
            # calculate how many j points to i point have same distance
            for j in xrange(n):
                if i == j:
                    continue
                dist = ((points[j][0] - points[i][0]) ** 2) + ((points[j][1] - points[i][1]) ** 2)
                hashmap[dist] += 1
            # loop hash
            for key, val in hashmap.iteritems():
                if val >= 2:
                    res += val * (val - 1)

        return res
