# bfs
class Solution:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        if prerequisites is None:
            return False
        if len(prerequisites) == 0:
            return True

        indegree = [0 for _ in range(numCourses)]
        graph = {i: set() for i in range(numCourses)}

        for end, start in prerequisites:
            if end not in graph[start]:
                indegree[end] += 1
            graph[start].add(end)

        return self.bfs(indegree, graph)

    def bfs(self, indegree, graph):
        q = collections.deque([i for i in range(len(indegree)) if indegree[i] == 0])
        while q:
            curr_node = q.popleft()
            for node in graph[curr_node]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)
        for d in indegree:
            if d != 0:
                return False
        return True


# dfs
class Solution:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        if prerequisites is None:
            return False
        if len(prerequisites) == 0:
            return True

        visited = [0 for _ in range(numCourses)]
        graph = {i: [] for i in range(numCourses)}

        for end, start in prerequisites:
            graph[start].append(end)

        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        visited[i] = 1
        return True
