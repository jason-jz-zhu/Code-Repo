class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n == 0:
            return False
        if len(edges) != n - 1:
            return False

        graph = {i: set([]) for i in xrange(n)}
        for item in edges:
            graph[item[0]].add(item[1])
            graph[item[1]].add(item[0])

        visited = [False for i in range(n)]
        return self.bfs(0, graph, visited)

    def bfs(self, i, graph, visited):
        q = collections.deque([i])
        while q:
            t = q.popleft()
            # check circle
            if visited[t]:
                return False
            visited[t] = True
            for node in graph[t]:
                q.append(node)
                graph[node].remove(t)
        # check weather not visited
        for i in range(len(visited)):
            if not visited[i]:
                return False
        return True
