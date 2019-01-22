class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if wall is None or len(wall) == 0 or len(wall[0]) == 0:
            return -1

        hashmap = collections.defaultdict(int)
        for i in range(len(wall)):
            s = 0
            for j in range(len(wall[i]) - 1):
                s += wall[i][j]
                hashmap[s] += 1
        vals = hashmap.values()
        maxVal = max(vals) if vals else 0
        return len(wall) - maxVal
