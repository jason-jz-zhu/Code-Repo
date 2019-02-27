class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or len(maze) == 0 or len(maze[0]) == 0:
            return False
        visited = set()
        return self.bfs(maze, start, destination, visited)

    def bfs(self, maze, start, destination, visited):
        dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
        q = collections.deque([(start[0], start[1])])
        visited.add(tuple((start[0], start[1])))
        while q:
            maze_x, maze_y = q.popleft()
            if [maze_x, maze_y] == destination:
                return True
            for k in range(4):
                x, y = maze_x + dx[k], maze_y + dy[k]
                while 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
                    x += dx[k]
                    y += dy[k]

                if (x - dx[k], y - dy[k]) not in visited:
                    q.append((x - dx[k], y - dy[k]))
                    visited.add(tuple((x - dx[k], y - dy[k])))
        return False
