class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]

        degree = [0 for _ in range(n)]
        graph = {i: [] for i in range(n)}

        for i, j in edges:
            degree[i] += 1
            degree[j] += 1
            graph[i].append(j)
            graph[j].append(i)

        leaves = [i for i in range(n) if degree[i] == 1]
        nodes_number = n
        while nodes_number > 2:
            tmp = []
            for leave in leaves:
                degree[leave] = 0
                nodes_number -= 1
                for i in graph[leave]:
                    degree[i] -= 1
                    if degree[i] == 1:
                        tmp.append(i)
            leaves = tmp
        return leaves
