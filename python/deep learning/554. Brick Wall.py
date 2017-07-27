class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if wall is None or len(wall) == 0 or len(wall[0]) == 0:
            return None
        map = collections.defaultdict(int)
        for i in xrange(len(wall)):
            sum = 0
            for j in xrange(len(wall[i]) - 1):
                sum += wall[i][j]
                map[sum] = map.get(sum, 0) + 1
        max_f = 0
        for key, val in map.items():
            max_f = max(val, max_f)

        return len(wall) - max_f
                
