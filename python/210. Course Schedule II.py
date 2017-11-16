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
        graph = {i: [] for i in xrange(numCourses)}
        for end, start in prerequisites:
            degree[end] += 1
            graph[start].append(end)

        res = []
        return self.bfs(degree, graph, numCourses, res)

    def bfs(self, degree, graph, numCourses, res):
        q = collections.deque([i for i in range(len(degree)) if degree[i] == 0])
        while q:
            t = q.popleft()
            res.append(t)
            for node in graph[t]:
                degree[node] -= 1
                if degree[node] == 0:
                    q.append(node)
        if len(res) == numCourses:
            return res
        return []
        
