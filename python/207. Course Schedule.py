class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if prerequisites is None:
            return False
        if len(prerequisites) == 0:
            return True

        degree = [0 for _ in range(numCourses)]
        graph = {i: [] for i in range(numCourses)}
        for end, start in prerequisites:
            degree[end] += 1
            graph[start].append(end)

        return self.bfs(degree, graph)

    def bfs(self, degree, graph):
        q = collections.deque([i for i in range(len(degree)) if degree[i] == 0])
        while q:
            t = q.popleft()
            for node in graph[t]:
                degree[node] -= 1
                if degree[node] == 0:
                    q.append(node)
        for i in degree:
            if degree[i] != 0:
                return False
        return True
        
