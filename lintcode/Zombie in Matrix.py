class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer
    PEOPLE = 0
    ZOMBIE = 1
    WALL = 2
    dX = [1, 0, 0, -1]
    dY = [0, 1, -1, 0]
    def zombie(self, grid):
        # Write your code here
        row = len(grid)
        col = len(grid[0])
        if grid is None or row is None or col is None:
            return 0
        q = []
        people = 0
        days = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == self.ZOMBIE:
                    q.append((i, j))
                if grid[i][j] == self.PEOPLE:
                    people += 1

        # bfs
        while q:
            days += 1
            new_q = []
            for node in q:
                node_x, node_y = node
                for k in xrange(4):
                    x = node_x + self.dX[k]
                    y = node_y + self.dY[k]
                    if not self.isPeople(x, y, grid):
                        continue
                    grid[x][y] = self.ZOMBIE
                    people -= 1
                    if people == 0:
                        return days
                    else:
                        new_q.append((x, y))
            q = new_q
        return -1

    def isPeople(self, x, y, grid):
        row = len(grid)
        col = len(grid[0])

        if x < 0 or x >= row:
            return False
        if y < 0 or y >= col:
            return False

        return grid[x][y] == self.PEOPLE
