# bfs
class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        wall = -1
        gate = 0
        unkown = 2 ** 31 -1
        q = collections.deque([])
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j)

        return


    def bfs(self, rooms, i, j):
        dir_x, dir_y = [-1, 0, 0, 1], [0, 1, -1, 0]
        q = collections.deque([(i, j)])
        while q:
            x, y = q.popleft()
            for k in range(4):
                grid_x, grid_y = x + dir_x[k], y + dir_y[k]
                if grid_x < 0 or grid_x >= len(rooms) or grid_y < 0 or grid_y >= len(rooms[0]) or rooms[grid_x][grid_y] < rooms[x][y] + 1:
                    continue
                rooms[grid_x][grid_y] = rooms[x][y] + 1
                q.append((grid_x, grid_y))



# Level order
class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        wall = -1
        gate = 0
        unkown = 2 ** 31 -1
        currLevel = []
        dir_x, dir_y = [-1, 0, 0, 1], [0, 1, -1, 0]
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    currLevel.append((i, j))

        while currLevel:
            nextLevel = []
            for i, j in currLevel:
                currDist = rooms[i][j]
                for k in range(4):
                    grid_x, grid_y = i + dir_x[k], j + dir_y[k]
                    if grid_x < 0 or grid_x >= len(rooms) or grid_y < 0 or grid_y >= len(rooms[0]) or rooms[grid_x][grid_y] != unkown:
                        continue
                    rooms[grid_x][grid_y] = currDist + 1
                    nextLevel.append((grid_x, grid_y))
            currLevel = nextLevel
        return
