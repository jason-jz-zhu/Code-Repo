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
        graph = {i: [] for i in range(numCourses)}
        for end, start in prerequisites:
            degree[end] += 1
            graph[start].append(end)

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
