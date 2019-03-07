class UnionFind:
    def __init__(self, size):
        self.father = [i for i in range(size)]
        self.count = size

    def find(self, node):
        if node == self.father[node]:
            return node
        self.father[node] = self.find(self.father[node])
        return self.father[node]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.count -= 1

    def query(self):
        return self.count

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        n = len(grid)
        uf = UnionFind(n * n * 4)

        for i in range(n):
            for j in range(n):
                index = 4 * (i * n + j)
                if grid[i][j] == '/':
                    uf.union(index + 0, index + 3)
                    uf.union(index + 1, index + 2)
                elif grid[i][j] == '\\':
                    uf.union(index + 0, index + 1)
                    uf.union(index + 2, index + 3)
                else:
                    uf.union(index + 0, index + 1)
                    uf.union(index + 1, index + 2)
                    uf.union(index + 2, index + 3)

                if i + 1 < n:
                    uf.union(index + 2, index + 4 * n + 0)
                if j + 1 < n:
                    uf.union(index + 1, index + 4 + 3)

        return uf.query()
