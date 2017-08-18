class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = {i: set([]) for i in xrange(n)}
        for item in edges:
            graph[item[0]].add(item[1])
            graph[item[1]].add(item[0])
        res = 0
        for i in xrange(n):
            q = [i]
            res += 1 if i in graph else 0
            while q:
                curr = q.pop()
                if curr in graph:
                    q += graph[curr]
                    del graph[curr]
        return res


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = [0] * n
        graph = {i: set([]) for i in xrange(n)}
        for item in edges:
            graph[item[0]].add(item[1])
            graph[item[1]].add(item[0])
        res = 0
        for i in xrange(n):
            if not visited[i]:
                self.dfs(i, graph, visited)
                res += 1
        return res

    def dfs(self, i, graph, visited):
        if visited[i]:
            return
        visited[i] = 1
        for x in graph[i]:
            self.dfs(x, graph, visited)
