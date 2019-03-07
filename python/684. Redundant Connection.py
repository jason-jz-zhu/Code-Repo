# dfs
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges or len(edges) == 0 or len(edges[0]) == 0:
            return []
        graph = collections.defaultdict(list)
        for start, end in edges:
            if self.has_path(-1, start, end, graph):
                return [start, end]
            graph[start].append(end)
            graph[end].append(start)
        return []

    def has_path(self, prev, start, end, graph):
        if start == end:
            return True
        if start not in graph or end not in graph:
            return False
        for neighbor in graph[start]:
            if neighbor == prev:
                continue
            if self.has_path(start, neighbor, end, graph):
                return True
        return False


# union find
class UnionFind:
    def __init__(self, n):
        self.father = [i for i in range(n + 1)]

    def find(self, node):
        if node == self.father[node]:
            return node
        self.father[node] = self.find(self.father[node])
        return self.father[node]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.father[root_x] = root_y
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for start, end in edges:
            if not uf.union(start, end):
                return [start, end]
        return []

# bfs
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if not edges or len(edges) == 0 or len(edges[0]) == 0:
            return []
        graph = collections.defaultdict(list)
        for start, end in edges:
            if self.has_path(start, end, graph, set()):
                return [start, end]
            graph[start].append(end)
            graph[end].append(start)
        return []

    def has_path(self, start, end, graph, visited):
        q = collections.deque([start])
        visited.add(start)
        while q:
            curr = q.popleft()
            if curr == end:
                return True
            for neighbor in graph[curr]:
                if neighbor in visited:
                    continue
                q.append(neighbor)
                visited.add(neighbor)
        return False
