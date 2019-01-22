class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        heap = []
        for point in points:
            dis = self.calDist(point)
            heapq.heappush(heap, (-dis, point))
            if len(heap) > K:
                heapq.heappop(heap)
        return [point for dis, point in heap]

    def calDist(self, point):
        return point[0] ** 2 + point[1] ** 2

class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
