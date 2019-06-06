class UnionFind:
    def __init__(self):
        self.father = {}
        self.count = 0

    def find(self, node):
        if node == self.father[node]:
            return node
        self.father[node] = self.find(self.father[node])
        return self.father[node]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count -= 1

    def query(self):
        return self.count

    def set_father(self, x):
        self.father[x] = x
        self.count += 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        if not positions or len(positions) == 0 or len(positions[0]) == 0:
            return []

        res = []
        uf = UnionFind()
        dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
        for p in positions:
            p_x, p_y = p
            p_index = p_x * n + p_y
            if p_index not in uf.father:
                uf.set_father(p_index)
            for k in range(4):
                x, y = p_x + dx[k], p_y + dy[k]
                index = x * n + y
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if index in uf.father:
                    uf.union(p_index, index)
            res.append(uf.query())
        return res
