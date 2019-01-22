class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if points is None or len(points) < 3:
            return 0
        res = 0
        size = len(points)
        for i in range(size):
            hashmap = collections.defaultdict(int)
            for j in range(size):
                if i == j:
                    continue
                dist = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                hashmap[dist] += 1
            for k, v in hashmap.items():
                if v > 1:
                    res += v * (v - 1)
        return res
