class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        hashset = set()
        for i in range(4):
            for j in range(i + 1, 4):
                dist = self.cal_dist(points[i], points[j])
                hashset.add(dist)
        return 0 not in hashset and len(hashset) == 2

    def cal_dist(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
