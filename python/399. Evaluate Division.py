# dfs
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            graph[x][y] = v
            graph[y][x] = 1.0 / v
        res = [self.dfs(x, y, set(), graph) if x in graph and y in graph else -1.0 for x, y in queries]
        return res

    def dfs(self, start, end, visited, graph):

        if start not in graph:
            return -1.0
        if start == end:
            return 1.0
        if start in graph and end in graph[start]:
            return graph[start][end]
        visited.add(start)
        for n in graph[start]:
            if n in visited:
                continue
            d = self.dfs(n, end, visited, graph)
            if d > 0:
                return d * graph[start][n]
        return -1.0

# union find
class UnionFind:
    def __init__(self, equations, values):
        self.father = {}
        for (x, y), v in zip(equations, values):
            if x not in self.father and y not in self.father:
                self.father[x] = (y, v)
                self.father[y] = (y, 1.0)
            elif x not in self.father:
                self.father[x] = (y, v)
            elif y not in self.father:
                self.father[y] = (x, 1.0 / v)
            else:
                root_x, v_x = self.find(x)
                root_y, v_y = self.find(y)
                self.father[root_x] = (root_y, v / v_x * v_y)

    def find(self, node):
        if node == self.father[node][0]:
            return self.father[node]
        x, v = self.find(self.father[node][0])
        self.father[node] = (x, self.father[node][1] * v)
        return self.father[node]

    def query(self, x, y):
        root_x, v_x = self.find(x)
        root_y, v_y = self.find(y)
        if root_x != root_y:
            return -1.0
        return v_x / v_y

    def get_father(self):
        return self.father

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
            uf = UnionFind(equations, values)
            father = uf.get_father()
            res = [uf.query(x, y) if x in father and y in father else -1.0 for (x, y) in queries]
            return res


# bfs
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for (x, y), v in zip(equations, values):
            graph[x].append((y, v))
            graph[y].append((x, 1.0 / v))
        res = [self.bfs(x, y, graph) if x in graph and y in graph else -1.0 for x, y in queries]
        return res

    def bfs(self, start, end, graph):
        if start not in graph or end not in graph:
            return -1.0

        q = collections.deque([(start, 1.0)])
        visited = set()
        visited.add(start)
        while q:
            curr_node, curr_product = q.popleft()
            if curr_node == end:
                return curr_product
            for neighbor, value in graph[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, curr_product * value))
        return -1.0
