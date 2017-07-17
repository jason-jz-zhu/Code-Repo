# Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
# return [[1,1],[2,5],[4,4]]


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

import heapq

class Type:
    def __init__(self, dist, point):
        self.dist = dist
        self.point = point

    def __cmp__(self, other):
        if other.dist != self.dist:
            return other.dist - self.dist
        if other.point.x != self.point.x:
            return other.point.x - self.point.x
        return other.point.y - self.point.y

class Solution:
    # @param {Pint[]} points a list of points
    # @param {Point} origin a point
    # @param {int} k an integer
    # @return {Pint[]} the k closest points
    def kClosest(self, points, origin, k):
        # Write your code here
        self.heap = []
        for point in points:
            dist = self.get_distance(point, origin)
            heapq.heappush(self.heap, Type(dist, point))
            if len(self.heap) > k:
                heapq.heappop(self.heap)

        res = []
        while len(self.heap) > 0:
            res.append(heapq.heappop(self.heap).point)

        res.reverse()

        return res

    def get_distance(self, a, b):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2
