class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        color = 2
        areas = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    areas[color] = self.get_area_dfs(grid, i, j, color)
                    color += 1
        max_area = max(areas.values() or [0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    area = 1
                    for color in self.get_color_bfs(grid, i, j):
                        area += areas[color]
                    max_area = max(max_area, area)
        return max_area

    def get_area_dfs(self, grid, i, j, color):
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return 0
        grid[i][j] = color
        s = 0
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            s += self.get_area_dfs(grid, x, y, color)
        return s + 1

    def get_color_bfs(self, grid, i, j):
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        colors = set()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                colors.add(grid[x][y])
        return colors
                    
