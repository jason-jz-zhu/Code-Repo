class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        degree = {i: 0 for i in xrange(n)}
        graph = {i: [] for i in xrange(n)}

        for i, j in edges:
            degree[i] += 1
            degree[j] += 1
            graph[i].append(j)
            graph[j].append(i)

        leaves = [i for i in xrange(n) if degree[i] == 1]
        nodes = n
        while nodes > 2:
            tmp = []
            for i in leaves:
                degree[i] = 0
                nodes -= 1
                for j in graph[i]:
                    degree[j] -= 1
                    if degree[j] == 1:
                        tmp.append(j)
            leaves = tmp
        return leaves
