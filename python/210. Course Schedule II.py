class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {int[]} the course order
    def findOrder(self, numCourses, prerequisites):
        # Write your code here
        degree = {i: 0 for i in xrange(numCourses)}
        edges = {i: [] for i in xrange(numCourses)}
        for end, start in prerequisites:
            degree[end] += 1
            edges[start].append(end)

        q = collections.deque([i for i in degree if degree[i] == 0])
        order = []
        while q:
            head = q.popleft()
            order.append(head)
            for node in edges[head]:
                degree[node] -= 1
                if degree[node] == 0:
                    q.append(node)
        if len(order) == numCourses:
            return order
        return []
