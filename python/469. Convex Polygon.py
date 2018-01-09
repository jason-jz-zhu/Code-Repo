class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if points is None or len(points) < 3:
            return False
        prev = 0
        size = len(points)
        for i in range(size):
            a = self.helper(points[i], points[(i + 1) % size], points[(i + 2) % size])
            if a == 0:
                continue
            if not prev:
                prev = a
            elif a * prev < 0:
                return False
        return True

    def helper(self, a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
            
