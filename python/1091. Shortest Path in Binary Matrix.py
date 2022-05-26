class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        ans = 1
        q = deque([(0, 0, 1)])
        visited = set()
        while q:
            i, j, dist = q.popleft()
            if i == n - 1 and j == n - 1:
                return dist
            for d1, d2 in dirs:
                x, y = i + d1, j + d2
                if 0 <= x < n and 0 <= y < n:
                    if (x, y) not in visited and grid[x][y] == 0:
                        visited.add((x, y))
                        q.append((x, y, dist + 1))
        return -1
