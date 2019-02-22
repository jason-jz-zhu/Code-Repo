class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if prerequisites is None:
            return []

        degree = [0 for _ in range(numCourses)]
        graph = {i: set() for i in range(numCourses)}
        for end, start in prerequisites:
            if end not in graph[start]:
                degree[end] += 1
            graph[start].add(end)

        return self.bfs(degree, graph)

    def bfs(self, degree, graph):
        res = []
        q = collections.deque([i for i in range(len(degree)) if degree[i] == 0])
        while q:
            c = q.popleft()
            res.append(c)
            for node in graph[c]:
                degree[node] -= 1
                if degree[node] == 0:
                    q.append(node)
        if len(res) == len(degree):
            return res
        return []


# dfs
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        if prerequisites is None:
            return False
        if len(prerequisites) == 0:
            return True

        visited = [0 for _ in range(numCourses)]
        graph = {i: [] for i in range(numCourses)}
        res = []
        for end, start in prerequisites:
            graph[start].append(end)

        for i in range(numCourses):
            if not self.dfs(graph, visited, i, res):
                return {}
        return res[::-1]

    def dfs(self, graph, visited, i, res):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for j in graph[i]:
            if not self.dfs(graph, visited, j, res):
                return False
        visited[i] = 1
        res.append(i)
        return True
