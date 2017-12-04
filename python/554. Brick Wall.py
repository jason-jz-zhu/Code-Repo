class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if wall is None or len(wall) == 0 or len(wall[0]) == 0:
            return None

        hashmap = collections.defaultdict(int)
        for i in range(len(wall)):
            s = 0
            for j in range(len(wall[i]) - 1):
                s += wall[i][j]
                hashmap[s] += 1

        max_fit = 0
        for val in hashmap.values():
            max_fit = max(max_fit, val)

        return len(wall) - max_fit
