# topological
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        for end, start in prerequisites:
            indegree[end] += 1
            graph[start].append(end)
        
        q = deque([node for node in range(numCourses) if indegree[node] == 0])
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        return ans if len(ans) == numCourses else None


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
