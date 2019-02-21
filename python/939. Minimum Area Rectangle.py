class Solution:
    def minAreaRect(self, points: 'List[List[int]]') -> 'int':
        if not points or len(points) == 0:
            return 0
        points = list(map(tuple, points))
        hashset = set(points)
        size = len(points)
        res = float('inf')
        for i in range(size - 1):
            p1 = points[i]
            for j in range(i + 1, size):
                p4 = points[j]
                if p1[0] == p4[0] or p1[1] == p4[1]:
                    continue
                p2 = (p1[0], p4[1])
                p3 = (p4[0], p1[1])
                if p2 in hashset and p3 in hashset:
                    res = min(res, abs(p1[0] - p3[0]) * abs(p1[1] - p2[1]))
        return res if res != float('inf') else 0

class Solution:
    def minAreaRect(self, points: 'List[List[int]]') -> 'int':
        if points is None or len(points) == 0:
            return 0

        x_ys = collections.defaultdict(list)
        for point in points:
            x_ys[point[0]].append(point[1])
        last_x = {}
        res = float('inf')
        for x in sorted(x_ys):
            ys = x_ys[x]
            ys.sort()
            for j, y2 in enumerate(ys):
                for i in range(j):
                    y1 = ys[i]
                    if (y1, y2) in last_x:
                        res = min(res, (y2 - y1) * (x - last_x[y1, y2]))
                    last_x[y1, y2] = x
        return res if res != float('inf') else 0
