# bfs
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if edges is None:
            return 0
        if n == 1 and len(edges) == 0:
            return 1

        graph = {i: set([]) for i in range(n)}
        for pair in edges:
            graph[pair[0]].add(pair[1])
            graph[pair[1]].add(pair[0])

        res = 0
        visited = [False for _ in range(n)]
        for i in range(n):
            if not visited[i]:
                self.bfs(i, graph, visited)
                res += 1
        return res

    def bfs(self, i, graph, visited):
        q = collections.deque([i])
        while q:
            t = q.popleft()
            visited[t] = True
            for node in graph[t]:
                if not visited[node]:
                    q.append(node)


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if edges is None:
            return 0
        if n == 1 and len(edges) == 0:
            return 1

        graph = {i: set([]) for i in range(n)}
        for pair in edges:
            graph[pair[0]].add(pair[1])
            graph[pair[1]].add(pair[0])

        res = 0
        visited = [False for _ in range(n)]
        for i in range(n):
            if not visited[i]:
                self.dfs(i, graph, visited)
                res += 1
        return res

    def dfs(self, i, graph, visited):
        visited[i] = True
        for node in graph[i]:
            if not visited[node]:
                self.dfs(node, graph, visited)
