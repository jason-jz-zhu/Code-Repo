class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points = [p1, p2, p3, p4]
        hashmap = collections.defaultdict(int)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                hashmap[self.helper(points[i], points[j])] += 1
        return len(hashmap) == 2 and 4 in hashmap.values() and 2 in hashmap.values()

    def helper(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
