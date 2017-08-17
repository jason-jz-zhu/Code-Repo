class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degree = {i: 0 for i in xrange(numCourses)}
        edges = {i: [] for i in xrange(numCourses)}
        for end, start in prerequisites:
            degree[end] += 1
            edges[start].append(end)

        q = collections.deque([i for i in degree if degree[i] == 0])
        while q:
            curr = q.popleft()
            for node in edges[curr]:
                degree[node] -= 1
                if degree[node] == 0:
                    q.append(node)
        for i in degree:
            if degree[i] != 0:
                return False
        return True
