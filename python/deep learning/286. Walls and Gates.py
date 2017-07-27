from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        q = deque()
        dir_x, dir_y = [0, 1, -1, 0],  [1, 0, 0, -1]
        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for k in xrange(4):
                grid_x, grid_y = i + dir_x[k], j + dir_y[k]
                if grid_x < 0 or grid_x >= len(rooms) or grid_y < 0 or grid_y >= len(rooms[0]) or rooms[grid_x][grid_y] < rooms[i][j] + 1:
                    continue
                rooms[grid_x][grid_y] = rooms[i][j] + 1
                q.append((grid_x, grid_y))
