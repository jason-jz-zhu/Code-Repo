class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0

        shapes = set([])
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    shape = []
                    self.dfs(grid, i, j, shape)
                    normalized_shape = self.normalize_shape(shape)
                    shapes.add(tuple(normalized_shape))
        return len(shapes)

    def dfs(self, grid, i, j, shape):
        dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
        shape.append((i, j))
        grid[i][j] = 2
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                continue
            if grid[x][y] == 1:
                self.dfs(grid, x, y, shape)

    def normalize_shape(self, shape):
        rotated_shapes = [[] for _ in range(8)]
        norm_res = []

        for p in shape:
            x, y = p
            rotated_shapes[0].append((x, y))
            rotated_shapes[1].append((-x, y))
            rotated_shapes[2].append((x, -y))
            rotated_shapes[3].append((-x, -y))
            rotated_shapes[4].append((y, x))
            rotated_shapes[5].append((-y, x))
            rotated_shapes[6].append((y, -x))
            rotated_shapes[7].append((-y, -x))

        for rs in rotated_shapes:
            rs.sort()

        for rs in rotated_shapes:
            tmp = [(0, 0)]
            for i in range(1, len(rs)):
                tmp.append((rs[i][0]-rs[0][0], rs[i][1]-rs[0][1]))
            norm_res.append(tmp[:])

        norm_res.sort()

        return norm_res[0]
