# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {boolean[][]} grid a chessboard included 0 (False) and 1 (True)
    # @param {Point} source a point
    # @param {Point} destination a point
    # @return {int} the shortest path
    dX = [1, 1, 2, 2, -1, -1, -2, -2]
    dY = [2, -2, 1, -1, 2, -2, 1, -1]
    row = 0
    col = 0
    EMPTY = 0
    BARRIER = 1
    def shortestPath(self, grid, source, destination):
        # Write your code here
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return -1
        self.row = len(grid)
        self.col = len(grid[0])

        q = collections.deque([(source.x, source.y)])
        step = 0
        while q:
            size = len(q)
            for i in xrange(size):
                source_x, source_y = q.popleft()
                if source_x == destination.x and source_y == destination.y:
                    return step
                for j in xrange(8):
                    x = source_x + self.dX[j]
                    y = source_y + self.dY[j]
                    if not self.isEmpty(x, y, grid):
                        continue
                    q.append((x, y))
                    grid[x][y] = 1
            step += 1
        return -1

    def isEmpty(self, x, y, grid):
        if x < 0 or x >= self.row:
            return False
        if y < 0 or y >= self.col:
            return False
        return grid[x][y] == 0
